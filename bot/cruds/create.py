import asyncio

import requests
from icecream import ic

from core.data.config import BASE_URL


async def create_user(user_id: int, username: str, name: str):
    # Check if user already exists
    loop = asyncio.get_running_loop()

    # Make the synchronous request in a separate thread
    check_response = await loop.run_in_executor(None, requests.get, f"{BASE_URL}/webhook/bot-users/{user_id}")
    if check_response.status_code == 404:
        create_response = await loop.run_in_executor(
            None,
            requests.post,
            f"{BASE_URL}/webhook/bot-users",
            {"user_id": user_id, "username": username, "name": name}
        )

        if create_response.status_code == 201:
            return {"message": "User created successfully.", "is_user_created": True}
        else:
            return {"message": "Failed to create user!", "is_user_created": False}
    elif check_response.status_code == 200:
        return {"message": "User already exists.", "is_user_created": False}
    else:
        return {"message": "Error checking user!", "is_user_created": False}


async def create_feedback(user, body: str):
    user = user.id
    ic(user, type(user))
    ic(body, type(body))
    loop = asyncio.get_running_loop()
    create_response = await loop.run_in_executor(
        None,
        requests.post,
        f"{BASE_URL}/webhook/feedbacks",
        {"user": user, "body": body}
    )
    ic(create_response.__dict__)
    ic(create_response.status_code)

    if create_response.status_code == 201:
        return {"message": "Feedback created successfully.", "is_feedback_created": True}
    else:
        return {"message": "Failed to create feedback!", "is_feedback_created": False}
