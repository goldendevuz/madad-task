import requests
from core.data.config import BASE_URL

def create_user(user_id: str, username: str, name: str):
    print(user_id, username, name)
    # Check if user already exists
    try:
        check_response = requests.get(f"{BASE_URL}/bot-users/{user_id}/")
    except Exception as e:
        print(e)
    
    if check_response.status_code == 404:  # User does not exist
        # Proceed to create the user
        create_response = requests.post(
            url=f"{BASE_URL}/bot-users/",
            json={"user_id": user_id, "username": username, "name": name}
        )
        
        if create_response.status_code == 201:
            return "User created successfully."
        else:
            return "Failed to create user:"
    elif check_response.status_code == 200:
        return "User already exists."
    else:
        return "Error checking user!"
