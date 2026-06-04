import asyncio


async def double_later(value):
    await asyncio.sleep(0)
    return value * 2


async def load_user_name(user_id, client):
    user = await client.get_user(user_id)
    return user["name"]
