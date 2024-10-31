import requests
from core.data.config import BASE_URL

def create_user(user_id: int, username: str, name: str):
    # Check if user already exists
    check_response = requests.get(f"{BASE_URL}/webhook/bot-users/{user_id}")
    
    if check_response.status_code == 404:  # User does not exist
        # Proceed to create the user
        create_response = requests.post(
            url=f"{BASE_URL}/webhook/bot-users",
            json={"user_id": user_id, "username": username, "name": name}
        )

        if create_response.status_code == 201:
            return {"message": "User created successfully.", "is_user_created": True}
        else:
            return {"message": "Failed to create user!", "is_user_created": False}
    elif check_response.status_code == 200:
        return {"message": "User already exists.", "is_user_created": False}
    else:
        return {"message": "Error checking user!", "is_user_created": False}