import unittest
from loader import replay


class ReplayTests(unittest.TestCase):
    def test_persisted_receipt(self):
        self.assertEqual(replay({"format": "v1", "cents": 123}), {"amount": 1.23, "version": 1})

    def test_current_receipt(self):
        self.assertEqual(replay({"format": "v2", "amount": 2}), {"amount": 2, "version": 2})
