import unittest

from qautils.slugify import slugify
from netutils.ports import parse_port


class TestSelectedSuiteCases(unittest.TestCase):
    def test_slugify_for_suite(self):
        self.assertEqual(slugify("Suite Test"), "suite-test")

    def test_parse_port_for_suite(self):
        self.assertEqual(parse_port("8080"), 8080)


if __name__ == "__main__":
    unittest.main()
