import unittest
from unittest.mock import patch

from labtools.config import build_url, get_mode


class TestConfigPatch(unittest.TestCase):
    def test_get_mode_from_env(self):
        with patch.dict("os.environ", {"APP_MODE": "test"}):
            self.assertEqual(get_mode(), "test")

    def test_get_mode_default(self):
        with patch.dict("os.environ", {}, clear=True):
            self.assertEqual(get_mode(), "dev")

    def test_patch_function(self):
        with patch("labtools.config.get_mode", return_value="stage"):
            self.assertEqual(build_url("example.com"), "https://example.com/stage")


if __name__ == "__main__":
    unittest.main()
