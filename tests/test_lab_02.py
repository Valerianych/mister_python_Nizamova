import unittest

from mister_python.math_tools import divide, is_even
from mister_python.text_tools import has_word, normalize_text, split_words


class TestLab02(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_is_even(self):
        self.assertTrue(is_even(8))

    def test_normalize_text(self):
        self.assertEqual(normalize_text("  Python  "), "python")

    def test_split_words(self):
        self.assertListEqual(split_words("python unittest test"), ["python", "unittest", "test"])

    def test_has_word(self):
        self.assertIn("python", split_words("python unittest"))
        self.assertTrue(has_word("python unittest", "python"))


if __name__ == "__main__":
    unittest.main()
