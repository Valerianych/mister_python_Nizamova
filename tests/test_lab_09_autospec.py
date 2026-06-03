import unittest
from unittest.mock import create_autospec

from labtools.users import UserRepository, UserService


class TestUserService(unittest.TestCase):
    def test_get_user_name(self):
        repository = create_autospec(UserRepository)
        repository.get_by_id.return_value = {"id": 1, "name": "Anna"}
        service = UserService(repository)

        self.assertEqual(service.get_user_name(1), "Anna")
        repository.get_by_id.assert_called_once_with(1)

    def test_get_user_name_returns_none(self):
        repository = create_autospec(UserRepository)
        repository.get_by_id.return_value = None
        service = UserService(repository)

        self.assertIsNone(service.get_user_name(99))


if __name__ == "__main__":
    unittest.main()
