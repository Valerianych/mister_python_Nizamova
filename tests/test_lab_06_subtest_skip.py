import sys
import unittest

from labtools.grades import grade_by_score


class TestGrades(unittest.TestCase):
    def test_grade_by_score_cases(self):
        cases = [
            (95, "excellent"),
            (70, "good"),
            (50, "pass"),
            (20, "fail"),
        ]
        for score, expected in cases:
            with self.subTest(score=score):
                self.assertEqual(grade_by_score(score), expected)

    def test_invalid_score(self):
        for score in (-1, 101):
            with self.subTest(score=score):
                with self.assertRaises(ValueError):
                    grade_by_score(score)

    @unittest.skipIf(sys.platform == "win32", "example skip on Windows")
    def test_skip_example(self):
        self.assertTrue(True)

    @unittest.expectedFailure
    def test_expected_failure_example(self):
        self.assertEqual(grade_by_score(49), "pass")


if __name__ == "__main__":
    unittest.main()
