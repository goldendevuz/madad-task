from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from django.utils.translation import gettext as _

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=_("❌ Bekor qilish"))],
    ],
    resize_keyboard=True
)

command_start = ReplyKeyboardMarkup(resize_keyboard=True,
                                    keyboard=[
                                        [
                                            KeyboardButton(text="🎓 Kurslar haqida ma'lumot"),
                                            KeyboardButton(text="📅 IT Xizmatlarimiz"),
                                        ],
                                        [
                                            KeyboardButton(text="💳 Muddatli to'lov haqida"),
                                            KeyboardButton(text="📝 Ro'yxatdan o'tish"),
                                        ],
                                        [
                                            KeyboardButton(text=_("📞 Bog'lanish")),
                                        ]
                                    ]
                                    )

# Kurslarni tanlash uchun klaviatura (misol)
def registration_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="IT kurslari"), KeyboardButton(text="Media kurslari")],
            [KeyboardButton(text="Boshqa xizmatlar")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard

def contact_request_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📱 Telefon raqamni yuborish", request_contact=True)]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )