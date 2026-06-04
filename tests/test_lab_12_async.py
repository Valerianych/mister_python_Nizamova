import unittest
from unittest.mock import AsyncMock

from labtools.async_service import double_later, load_user_name


class TestAsyncService(unittest.IsolatedAsyncioTestCase):
    async def test_double_later(self):
        result = await double_later(5)
        self.assertEqual(result, 10)

    async def test_load_user_name(self):
        client = AsyncMock()
        client.get_user.return_value = {"id": 1, "name": "Olga"}

        result = await load_user_name(1, client)

        self.assertEqual(result, "Olga")
        client.get_user.assert_awaited_once_with(1)


if __name__ == "__main__":
    unittest.main()
