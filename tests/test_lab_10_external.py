import unittest
from unittest.mock import Mock, patch

from labtools.external import current_year, get_profile


class TestExternalDependencies(unittest.TestCase):
    def test_current_year_with_patch(self):
        with patch("labtools.external.datetime") as fake_datetime:
            fake_datetime.now.return_value.year = 2030
            self.assertEqual(current_year(), 2030)

    def test_get_profile_from_client(self):
        client = Mock()
        client.get_user.return_value = {"name": "Ivan"}

        result = get_profile(1, client)

        self.assertEqual(result, {"id": 1, "name": "Ivan"})
        client.get_user.assert_called_once_with(1)


if __name__ == "__main__":
    unittest.main()
