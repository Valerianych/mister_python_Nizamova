import unittest

from shop.pricing import final_price_cents


class TestPricingIntegration(unittest.TestCase):
    def test_discount_and_tax_scenario(self):
        self.assertEqual(final_price_cents(1000, discount_percent=10, tax_percent=20), 1080)

    def test_zero_price_scenario(self):
        self.assertEqual(final_price_cents(0, discount_percent=0, tax_percent=20), 0)


if __name__ == "__main__":
    unittest.main()
