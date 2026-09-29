import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
sys.dont_write_bytecode = True
import _handoff_common as common


class RedactionTests(unittest.TestCase):
    def test_url_drops_userinfo_and_query(self):
        self.assertEqual(common.redact_url('https://user:tok@github.com/a/b.git'), 'https://github.com/a/b.git')
        self.assertEqual(common.redact_url('https://mcp.example.com/sse?key=abc'), 'https://mcp.example.com/sse')

    def test_args_redact_flag_value_and_assignment(self):
        self.assertEqual(common.redact_args(['--api-key', 'abc123', '--port', '80']),
                         ['--api-key', '<redacted>', '--port', '80'])
        self.assertEqual(common.redact_args(['TOKEN=xyz']), ['TOKEN=<redacted>'])

    def test_template_value_redaction(self):
        self.assertEqual(common.redact_value('OPENAI_API_KEY', 'sk-live'), '<redacted>')
        self.assertEqual(common.redact_value('PORT', '3000'), '3000')


if __name__ == '__main__':
    unittest.main()
