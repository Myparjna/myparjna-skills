import unittest
from price_order import price


class PriceTests(unittest.TestCase):
    def test_price(self):
        self.assertEqual(price({"quantity": 2, "unit_price": 5}), 10)
