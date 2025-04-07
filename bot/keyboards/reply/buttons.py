from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from django.utils.translation import gettext as _

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Yes"), KeyboardButton(text="❌ No")],  # Row 1
        # [KeyboardButton("Option 3")]                        # Row 2
    ],
    resize_keyboard=True
)

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
                                            KeyboardButton(text=_("📨 Taklif va shikoyatlar uchun")),
                                        ]
                                    ]
                                    )

courses_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Kompyuter Savodxonligi PRO"),
        KeyboardButton(text="Kompyuter Savodxonligi LIGHT"),
    ],
    [
        KeyboardButton(text="Grafik Dizayn Kursi"),
        KeyboardButton(text="Web Dasturlash (9 oy)"),
    ],
    [
        KeyboardButton(text="React JS Kursi (2 oy)"),
        KeyboardButton(text="Mobil Dasturlash (Flutter) - 9 oy"),
    ],
    [
        KeyboardButton(text="Mobilografiya Kursi (2 oy)"),
        KeyboardButton(text="Matematika Kursi"),
    ],
    [
        KeyboardButton(text="Arab Tili Kursi"),
        KeyboardButton(text="Nemis Tili Kursi (0 dan B1 darajagacha)"),
    ],
    [
        KeyboardButton(text="Rus Tili Kursi (0 dan B1 darajagacha)"),
        KeyboardButton(text="Ingliz Tili Kursi (0 dan B1 darajagacha)"),
    ],
    [
        KeyboardButton(text="Xalqaro IELTS Kursi"),
    ]
])
