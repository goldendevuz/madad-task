import gspread
from gspread_formatting import set_column_width
from icecream import ic

from bot.cruds.get_users import get_all_users


async def update_google_sheet():
    users = await get_all_users()
    # Initialize gspread with service account
    gc = gspread.service_account(filename='core/data/service_account.json')

    # Open the sheet
    wks = gc.open("Bot users").sheet1

    # Clear the existing data
    wks.clear()

    if users:
        # Create header row dynamically based on the keys of the first user
        header = list(users[0].keys())

        # Prepare the data to write to the sheet
        user_data = [header]  # Start with the header row

        # Add each user as a row in the sheet
        for user in users:
            user_data.append([user.get(key, "Unknown") for key in header])

        # Update the sheet with the new data
        wks.update(range_name="A1", values=user_data)

        # Center-align the data
        num_columns = len(header)
        range_to_format = f"A1:{chr(65 + num_columns - 1)}{len(user_data)}"

        wks.format(range_to_format, {'horizontalAlignment': 'CENTER'})

        # Format the header row to be bold
        wks.format(f'A1:{chr(65 + num_columns - 1)}1', {'textFormat': {'bold': True}})

        # Resize columns to fit the longest data in each column
        for col_num, col_name in enumerate(header, start=1):
            max_length = max(len(str(col_name)), max(len(str(user.get(col_name, ""))) for user in users))
            column_letter = chr(65 + col_num - 1)
            set_column_width(wks, column_letter, max_length * 10)
    else:
        ic("No users fetched, nothing to update.")
