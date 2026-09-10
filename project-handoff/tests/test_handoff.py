import importlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
import contextlib
import io
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
sys.dont_write_bytecode = True
a, p, c, g, v, common = [importlib.import_module(n) for n in (
    'analyze_project', 'plan_handoff', 'compare_handoff', 'generate_handoff', 'verify_handoff', '_handoff_common')]


class HandoffTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for mod in (a, p, c, g, v):
            patcher = patch.object(mod, 'ROOT', self.root)
            patcher.start()
            self.addCleanup(patcher.stop)
        self.docs = self.root / 'ProjectDoc'
        self.docs.mkdir()
        for mod, attr in ((a,'OUT_DIR'),(p,'DOC_DIR'),(c,'DOC_DIR'),(g,'OUT'),(v,'OUT')):
            patcher = patch.object(mod,attr,self.docs)
            patcher.start()
            self.addCleanup(patcher.stop)
        for attr in ('MAX_GREP_FILES','SKIP_DIRS','INCLUDE_DIRS','_SKIP_LOWER_CACHE'):
            value = getattr(a,attr)
            patcher=patch.object(a,attr,value.copy() if isinstance(value,(set,list)) else value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_secret_prose_does_not_mask_value(self):
        self.assertFalse(v._is_placeholder('ghp_'+'Ab3Cd4Ef5Gh6Ij7Kl8Mn9Op0Qr1St2Uv3Wx4', 'example documentation'))
        self.assertTrue(v._is_placeholder('sk-xxxxxxxxxxxxxxxxxxxxxxxx', ''))

    def test_eight_base_documents(self):
        names={'readme.md','usage.md','architecture.md','environment.md','deployment.md','operations.md','regression-test.md','known-issues.md'}
        self.assertEqual(set(p.BASE_DOCS),names)
        self.assertEqual(v.check_doc_count([self.docs/n for n in names]),[])

    def test_pyproject_dependencies(self):
        f=self.root/'pyproject.toml'
        f.write_text('[project]\ndependencies=["FastAPI>=0.1", "openai>=1", "sqlalchemy>=2"]\n[project.optional-dependencies]\ntest=["pytest>=8"]\n[dependency-groups]\ndev=["ruff", {include-group="test"}]\n',encoding='utf-8')
        deps=a.load_python_deps([], [f])
        self.assertTrue({'fastapi','openai','sqlalchemy','pytest','ruff'} <= deps.keys())

    def test_config_comments_and_shared_parser(self):
        (self.root/'.handoff.yml').write_text('skip_dirs: ["fixtures", "has#hash"] # comment\nmax_files: 5 # comment\n',encoding='utf-8')
        a.load_config()
        self.assertIn('fixtures',a.SKIP_DIRS)
        self.assertIn('has#hash',a.SKIP_DIRS)
        self.assertEqual(a.MAX_GREP_FILES,5)
        self.assertEqual(p.read_config()['max_files'],5)

    def test_shell_files_are_collected(self):
        samples={'launch.sh':'echo $SHELL_VALUE','launch.ps1':'Write-Output $env:POWERSHELL_VALUE','launch.cmd':'echo %CMD_VALUE%','Dockerfile':'ENV A=$DOCKER_VALUE'}
        for name,text in samples.items():
            (self.root/name).write_text(text,encoding='utf-8')
        texts,_=a.collect_source_texts()
        self.assertEqual({x[0] for x in texts},set(samples))
        used=set(a.detect_env_vars(texts)['used_in_code'])
        self.assertTrue({'SHELL_VALUE','POWERSHELL_VALUE','CMD_VALUE','DOCKER_VALUE'}<=used)

    def test_early_truncation_is_reported(self):
        a.MAX_GREP_FILES=2
        for i in range(9):
            (self.root/f'000-{i}.bin').write_bytes(b'x')
        (self.root/'z.py').write_text('value=1',encoding='utf-8')
        _,truncated=a.collect_source_texts()
        self.assertTrue(truncated)

    def test_broken_markdown_link(self):
        f=self.docs/'readme.md'
        f.write_text('[missing](./missing.md)\n[external](https://example.org)\n',encoding='utf-8')
        issues,_=v.check_doc(f,{})
        self.assertTrue(any(sev=='ERROR' and 'missing.md' in msg for sev,msg in issues))

    def test_business_change_not_preserved(self):
        for name in c.expected_docs({}):
            (self.docs/name).write_text('manual',encoding='utf-8')
        old={'source_file_fingerprints':{'business.py':{'sha256':'a'}}}
        new={'source_file_fingerprints':{'business.py':{'sha256':'b'}}}
        plan=c.make_plan(old,new)
        actions={x['document']:x['action'] for x in plan['recommendations']}
        self.assertEqual(actions['usage.md'],'review')
        self.assertEqual(actions['architecture.md'],'review')

    def report(self):
        (self.root/'package.json').write_text('{"name":"fixture"}',encoding='utf-8')
        with patch.object(Path,'home',return_value=self.root/'fake-home'), contextlib.redirect_stdout(io.StringIO()), patch.object(sys,'argv',['scan']):
            a.main()
        return json.loads((self.docs/'analysis-report.json').read_text(encoding='utf-8'))

    def generate(self, *args):
        with patch.object(g,'REPORT_PATH',self.docs/'analysis-report.json'), patch.object(g,'DEFAULT_PLAN_PATH',self.root/'TempScr/project-handoff-plan.json'), patch.object(sys,'argv',['generate',*args]),contextlib.redirect_stdout(io.StringIO()):
            g.main()

    def test_generator_balanced_and_optional_skip(self):
        report=self.report()
        report['api_routes']=['GET /hello (app.py)']
        report['desktop']=[{'type':'Electron','version':'1'}]
        (self.docs/'analysis-report.json').write_text(json.dumps(report),encoding='utf-8')
        folder=self.root/'TempScr'
        folder.mkdir()
        (folder/'project-handoff-plan.json').write_text(json.dumps({'documents':[{'name':'api.md','action':'skip'},{'name':'desktop.md','action':'skip'}]}),encoding='utf-8')
        self.generate()
        self.assertEqual({x.name for x in self.docs.glob('*.md')},set(p.BASE_DOCS))
        for f in self.docs.glob('*.md'):
            self.assertFalse(any('本地文档链接不存在' in msg for _,msg in v.check_doc(f,{})[0]))
        self.assertEqual(v.check_required_sections(list(self.docs.glob('*.md'))),[])

    def test_legacy_migration_preserves_manual_text(self):
        self.report()
        (self.docs/'MODULES.md').write_text('# 模块\n\n人工约定 123\n\n[维护](./MAINTENANCE.md)\n',encoding='utf-8')
        (self.docs/'MAINTENANCE.md').write_text('# 维护\n\n特殊经验 456\n',encoding='utf-8')
        self.generate('--mode','update')
        self.assertFalse(any(f.name.lower() in {'modules.md','maintenance.md'} for f in self.docs.glob('*.md')))
        self.assertIn('人工约定 123',(self.docs/'architecture.md').read_text(encoding='utf-8'))
        self.assertIn('特殊经验 456',(self.docs/'operations.md').read_text(encoding='utf-8'))
        self.assertTrue(list((self.root/'TempFiles').glob('*')))
        snapshot={f.name:f.read_bytes() for f in self.docs.glob('*.md')}
        self.generate('--mode','update')
        self.assertEqual(snapshot,{f.name:f.read_bytes() for f in self.docs.glob('*.md')})

    def test_source_fingerprint_is_written(self):
        (self.root/'business.py').write_text('def fee(): return 1',encoding='utf-8')
        before=self.report()
        (self.root/'business.py').write_text('def fee(): return 2',encoding='utf-8')
        after=self.report()
        self.assertIn('business.py',c.fingerprint_changes(before,after)['modified'])

    def test_verify_success_and_rebuild(self):
        report=self.report()
        self.generate()
        # Synthetic content checks the validator, not real business acceptance.
        for f in self.docs.glob('*.md'):
            content=re.sub(r'<!-- TODO\(AI\): .*? -->','[需向交接人确认: 隔离测试事项]',f.read_text(encoding='utf-8'),flags=re.S)
            f.write_text(content,encoding='utf-8')
        with patch.object(v,'REPORT_PATH',self.docs/'analysis-report.json'),contextlib.redirect_stdout(io.StringIO()):
            v.main()
        self.assertTrue((self.docs/'.handoff/analysis-report.verified.json').exists())
        snapshot=(self.docs/'usage.md').read_bytes()
        self.generate('--mode','update')
        self.assertEqual((self.docs/'usage.md').read_bytes(),snapshot)
        self.generate('--mode','rebuild')
        self.assertIn('TODO(AI)',(self.docs/'usage.md').read_text(encoding='utf-8'))
        self.assertTrue(list((self.root/'TempFiles').glob('ProjectDoc_backup_*')))

    def test_invalid_config_is_explicit(self):
        (self.root/'.handoff.yml').write_text('max_files: wrong',encoding='utf-8')
        with self.assertRaises(SystemExit):
            a.load_config()

    def test_git_dirty_change_drives_review(self):
        def git(*args):
            return subprocess.run(['git',*args],cwd=self.root,check=True,capture_output=True,text=True).stdout.strip()
        git('init','-q')
        (self.root/'business.py').write_text('value=1',encoding='utf-8')
        git('add','business.py')
        git('-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','-qm','fixture')
        old={'git':{'hash':git('rev-parse','HEAD')},'source_fingerprints_complete':True}
        (self.root/'business.py').write_text('value=2',encoding='utf-8')
        changes=c.git_changes_since_baseline(old)
        self.assertIn('business.py',changes['changed_files'])
        for name in c.expected_docs(old):
            (self.docs/name).touch()
        plan=c.make_plan(old,old,changes)
        self.assertEqual(next(x['action'] for x in plan['recommendations'] if x['document']=='usage.md'),'review')

    def test_custom_plan_is_used_by_validation(self):
        report=self.report()
        report['api_routes']=['GET /hello (app.py)']
        (self.docs/'analysis-report.json').write_text(json.dumps(report),encoding='utf-8')
        custom=self.root/'custom-plan.json'
        custom.write_text(json.dumps({'documents':[{'name':'api.md','action':'skip'}]}),encoding='utf-8')
        self.generate('--plan',str(custom))
        for f in self.docs.glob('*.md'):
            f.write_text(re.sub(r'<!-- TODO\(AI\): .*? -->','[需向交接人确认: 隔离测试事项]',f.read_text(encoding='utf-8'),flags=re.S),encoding='utf-8')
        with patch.object(v,'REPORT_PATH',self.docs/'analysis-report.json'),contextlib.redirect_stdout(io.StringIO()):
            v.main()


if __name__=='__main__':
    unittest.main()
