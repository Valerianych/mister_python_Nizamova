import unittest

from qautils.slugify import slugify


class TestSlugify(unittest.TestCase):
    def test_slugify_basic_text(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_slugify_multiple_spaces(self):
        self.assertEqual(slugify("  multiple   spaces  "), "multiple-spaces")

    def test_slugify_underscore(self):
        self.assertEqual(slugify("Already_Slug"), "already-slug")

    def test_slugify_many_dashes(self):
        self.assertEqual(slugify("---A---B---"), "a-b")

    def test_slugify_only_bad_symbols(self):
        self.assertEqual(slugify("!!!"), "")


if __name__ == "__main__":
    unittest.main()
