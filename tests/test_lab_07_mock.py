import unittest
from unittest.mock import Mock

from labtools.notifications import send_safe, send_welcome


class TestNotifications(unittest.TestCase):
    def test_send_welcome_calls_client(self):
        client = Mock()
        result = send_welcome("user@example.com", client)

        self.assertTrue(result)
        client.send.assert_called_once_with("user@example.com", "Welcome")

    def test_send_safe_returns_error(self):
        client = Mock()
        client.send.side_effect = RuntimeError("service error")

        result = send_safe("user@example.com", client)

        self.assertEqual(result, "error")


if __name__ == "__main__":
    unittest.main()
