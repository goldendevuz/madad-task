from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Yes"), KeyboardButton(text="❌ No")],  # Row 1
        # [KeyboardButton("Option 3")]                        # Row 2
    ],
    resize_keyboard=True
)