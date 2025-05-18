import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from icecream import ic

# Get the absolute path to the directory containing this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Navigate from bot/utils/ to core/data/
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, '..', '..', 'core', 'data', 'service-account.json')
SERVICE_ACCOUNT_FILE = os.path.abspath(SERVICE_ACCOUNT_FILE)
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def get_google_services():
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    sheets_service = build('sheets', 'v4', credentials=creds)
    return creds, sheets_service

def get_user_rows(sheet_id, sheet_name="responses"):
    range_name = f"{sheet_name}!A2:AA"  # First 4 columns (Timestamp, Name, Phone, Telegram)
    ic(sheet_id, range_name)
    _, sheets_service = get_google_services()

    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=range_name
    ).execute()
    ic(result)

    rows = result.get("values", [])
    user_rows = []
    for row in rows:
        if row[16] == rows[-2][16]:  # Check if the phone number is empty
            user_rows.append(row)
        # Check if the row is already in the database
        # if not BotUser.objects.filter(user_id=row[3]).exists():
        #     user_rows.append(row)
        # else:
        #     ic(f"User {row[3]} already exists in the database.")
    # ic(rows) #if rows else []
    return user_rows
