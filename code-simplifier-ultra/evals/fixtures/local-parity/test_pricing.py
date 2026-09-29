import unittest
from pricing import discount


class PricingTests(unittest.TestCase):
    def test_observable_results(self):
        for user, total, expected in [
            (None, 200, 0), ({}, 200, 0),
            ({"member": True}, 100, 0),
            ({"member": True}, 200, 20),
            ({"member": True}, float("nan"), 0),
            ({"member": True}, -1, 0),
        ]:
            with self.subTest(user=user, total=total):
                self.assertEqual(discount(user, total), expected)
