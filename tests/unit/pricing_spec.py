import unittest

from shop.pricing import final_price_cents


class TestFinalPrice(unittest.TestCase):
    def test_base_price_with_tax(self):
        self.assertEqual(final_price_cents(1000), 1200)

    def test_discount_100(self):
        self.assertEqual(final_price_cents(1000, discount_percent=100), 0)

    def test_tax_0(self):
        self.assertEqual(final_price_cents(1000, tax_percent=0), 1000)

    def test_invalid_negative_base(self):
        with self.assertRaises(ValueError):
            final_price_cents(-1)

    def test_invalid_discount_less_than_zero(self):
        with self.assertRaises(ValueError):
            final_price_cents(1000, discount_percent=-1)

    def test_invalid_discount_more_than_100(self):
        with self.assertRaises(ValueError):
            final_price_cents(1000, discount_percent=101)

    def test_invalid_tax_less_than_zero(self):
        with self.assertRaises(ValueError):
            final_price_cents(1000, tax_percent=-1)

    def test_invalid_tax_more_than_100(self):
        with self.assertRaises(ValueError):
            final_price_cents(1000, tax_percent=101)


if __name__ == "__main__":
    unittest.main()
