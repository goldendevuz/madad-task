import asyncio

import requests
from icecream import ic

from core.data.config import BASE_URL


async def get_all_users():
    loop = asyncio.get_running_loop()
    response = await loop.run_in_executor(None, requests.get, f"{BASE_URL}/webhook/bot-users")
    # Check if the request was successful
    if response.status_code == 200:
        # Process the JSON response
        users = response.json()
        # ic(users)
        return users
    else:
        # Handle errors if the request was unsuccessful
        ic(f"Failed to fetch bot users: {response.status_code}")
