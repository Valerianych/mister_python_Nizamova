import unittest

from labtools.diagnostics import old_sum, process_item


class TestDiagnostics(unittest.TestCase):
    def test_old_sum_warning(self):
        with self.assertWarns(DeprecationWarning):
            self.assertEqual(old_sum(2, 3), 5)

    def test_process_item_logs(self):
        with self.assertLogs("labtools", level="INFO") as logs:
            result = process_item(10)

        self.assertTrue(result)
        self.assertIn("item processed: 10", logs.output[0])


if __name__ == "__main__":
    unittest.main()
