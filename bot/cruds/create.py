import aiohttp
import asyncio
from icecream import ic
from core.data.config import BASE_URL

async def create_user(user_id: int, username: str, name: str):
    async with aiohttp.ClientSession() as session:
        # Check if user already exists
        async with session.get(f"{BASE_URL}/webhook/bot-users/{user_id}") as check_response:
            if check_response.status == 404:
                async with session.post(f"{BASE_URL}/webhook/bot-users", json={"user_id": user_id, "username": username, "name": name}) as create_response:
                    if create_response.status == 201:
                        return {"message": "User created successfully.", "is_user_created": True}
                    else:
                        return {"message": "Failed to create user!", "is_user_created": False}
            elif check_response.status == 200:
                return {"message": "User already exists.", "is_user_created": False}
            else:
                return {"message": "Error checking user!", "is_user_created": False}

async def create_feedback(user, body: str):
    async with aiohttp.ClientSession() as session:
        # Send feedback
        async with session.post(f"{BASE_URL}/webhook/feedbacks", json={"user": user.id, "body": body}) as create_response:
            ic(create_response.__dict__)
            ic(create_response.status)

            if create_response.status == 201:
                return {"message": "Feedback created successfully.", "is_feedback_created": True}
            else:
                return {"message": "Failed to create feedback!", "is_feedback_created": False}