import unittest

from netutils.ports import parse_port


class TestParsePort(unittest.TestCase):
    def test_valid_int_boundaries(self):
        cases = [
            (1, 1),
            (2, 2),
            (65534, 65534),
            (65535, 65535),
        ]

        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(parse_port(value), expected)

    def test_invalid_int_boundaries(self):
        for value in (0, -1, 65536):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_port(value)

    def test_valid_string_values(self):
        cases = [
            ("1", 1),
            (" 80 ", 80),
            ("65535", 65535),
        ]

        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(parse_port(value), expected)

    def test_invalid_string_values(self):
        for value in ("", "   ", "+80", "-1", "abc"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_port(value)

    def test_invalid_types(self):
        for value in (None, [], {}, 3.14, True, False):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    parse_port(value)


if __name__ == "__main__":
    unittest.main()
