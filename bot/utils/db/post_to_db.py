import requests

BASE_URL = "http://127.0.0.1:8000/api/bot/v1"

def create_user(user_id: str, username: str, name: str):
    requests.post(f"{BASE_URL}/users/", json={"user_id": user_id, "username": username, "name": name})