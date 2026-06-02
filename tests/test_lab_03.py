import unittest

from mister_python.math_tools import add


class TestLab03(unittest.TestCase):
    def test_unittest_discovery(self):
        self.assertEqual(add(1, 1), 2)


if __name__ == "__main__":
    unittest.main()
