import unittest

from tests.test_lab_05_suite import TestSelectedSuiteCases


loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromTestCase(TestSelectedSuiteCases))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
raise SystemExit(0 if result.wasSuccessful() else 1)
