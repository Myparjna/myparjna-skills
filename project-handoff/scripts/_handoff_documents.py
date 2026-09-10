"""Shared document selection for the balanced handoff layout."""
import json
from pathlib import Path

BASE_DOCS = ['readme.md', 'usage.md', 'architecture.md', 'environment.md',
             'deployment.md', 'operations.md', 'regression-test.md', 'known-issues.md']
TOPIC_DOCS = {'ai-services.md', 'api.md', 'database.md', 'desktop.md'}
LEGACY_DOCS = {'modules.md': 'architecture.md', 'infrastructure.md': 'deployment.md',
               'maintenance.md': 'operations.md', 'runbook.md': 'operations.md'}
REQUIRED_SECTIONS = {
    'readme.md': ['待确认问题', '项目简介', '核心功能', '技术栈', '快速启动', '速查卡', '文档导航'],
    'usage.md': ['适用角色与入口', '核心使用流程', '启动与停止'],
    'architecture.md': ['架构总览', '目录结构', '技术选型与路线', '模块职责矩阵', '关键调用链'],
    'environment.md': ['变量清单', '密钥轮换'],
    'deployment.md': ['首次完整部署演练', '域名与 DNS', '第三方服务账号清单'],
    'operations.md': ['监控与日志', '例行检查清单', '回滚', '常见故障处置'],
    'regression-test.md': ['测试现状', '回归范围', '发布前最小回归清单', '已知测试缺口'],
    'known-issues.md': ['已知 Bug', '技术债'],
    'ai-services.md': ['使用的 SDK', '计费与限额'],
    'api.md': ['接口清单（扫描所得）', '鉴权'],
    'database.md': ['概况', '数据模型', '备份与恢复'],
    'desktop.md': [],
}


def conditional_docs(report):
    ai = report.get('ai_services', {})
    db = report.get('database', {})
    return [
        ('ai-services.md', bool(ai.get('sdks') or ai.get('endpoints') or ai.get('model_names')), 'AI SDK/API 或模型线索'),
        ('api.md', bool(report.get('api_routes') or report.get('api_specs')), 'API 路由或规范'),
        ('database.md', bool(db.get('clients') or db.get('orm')), '数据库或 ORM'),
        ('desktop.md', bool(report.get('desktop')), '桌面端配置'),
    ]


def default_docs(report):
    return set(BASE_DOCS) | {name for name, detected, _ in conditional_docs(report) if detected}


def load_document_plan(root, path=None):
    path = Path(path) if path else root / 'TempScr' / 'project-handoff-plan.json'
    if not path.exists():
        return {}
    try:
        plan = json.loads(path.read_text(encoding='utf-8'))
        if not isinstance(plan, dict) or not isinstance(plan.get('documents', []), list):
            raise ValueError('documents 必须为列表')
        if plan.get('project_root') and Path(plan['project_root']).resolve() != root.resolve():
            raise ValueError('计划属于其他项目，请重新生成')
        return plan
    except (OSError, ValueError) as exc:
        raise SystemExit(f'ERROR: 无法读取交接计划 {path}: {exc}') from exc


def selected_docs(report, plan=None):
    selected = default_docs(report)
    for item in (plan or {}).get('documents', []):
        name = item['name'].lower()
        # Old separate-document decisions never remove the merged destination.
        if name in LEGACY_DOCS:
            continue
        if name not in set(BASE_DOCS) | TOPIC_DOCS:
            raise SystemExit(f'ERROR: 未知交接文档: {name}')
        if item.get('action') == 'skip':
            if name in BASE_DOCS:
                raise SystemExit(f'ERROR: 平衡版基础文档不可跳过: {name}')
            selected.discard(name)
        elif item.get('action') in ('generate', 'create', 'update', 'review', 'preserve'):
            selected.add(name)
    return selected


def applied_docs(root, report):
    path = root / 'ProjectDoc' / '.handoff' / 'document-selection.json'
    return selected_docs(report, load_document_plan(root, path) if path.exists() else load_document_plan(root))
