from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Inline buttons
inline_menu = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="✅ Yes", callback_data='yes'),
            InlineKeyboardButton(text="❌ No", callback_data='no')
        ]
    ]
)