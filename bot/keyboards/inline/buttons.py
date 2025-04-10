from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from django.utils.translation import gettext as _

def services_inline_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=_("🚀 Sun’iy intellekt (AI) xizmatlari"), callback_data="ai_services"),
                InlineKeyboardButton(text=_("💻 IT xizmatlari"), callback_data="it_services"),
            ],
            [
                InlineKeyboardButton(text=_("🎨 Grafik Dizayn va Media xizmatlari"), callback_data="design_services"),
            ],
            [
                InlineKeyboardButton(text=_("💡 Barcha xizmatlar"), callback_data="all_services")
            ]
        ]
    )

def close_popup_keyboard():
    close_button = InlineKeyboardButton(_("❌ Yopish"), callback_data="close_popup")
    close_keyboard = InlineKeyboardMarkup(inline_keyboard=[[close_button]])
    return close_keyboard

def contact_inline_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐 Website", url="https://madad.top/"),
            InlineKeyboardButton(text="📍 Lokatsiya", url="https://www.google.com/maps?q=40.5455591,70.8870326")
        ],
        [
            InlineKeyboardButton(text="▶️ YouTube", url="https://www.youtube.com/@madadtalim/videos"),
            InlineKeyboardButton(text="📸 Instagram", url="https://www.instagram.com/madad.talim/")
        ],
    ])
    return keyboard

courses_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text=_("💻 Kompyuter Savodxonligi PRO"), callback_data="course_pro"),
        InlineKeyboardButton(text=_("🖥 Kompyuter Savodxonligi LIGHT"), callback_data="course_light"),
    ],
    [
        InlineKeyboardButton(text=_("🎨 Grafik Dizayn Kursi"), callback_data="course_design"),
        InlineKeyboardButton(text=_("🌐 Web Dasturlash (9 oy)"), callback_data="course_web"),
    ],
    [
        InlineKeyboardButton(text=_("⚛️ React JS Kursi (2 oy)"), callback_data="course_react"),
        InlineKeyboardButton(text=_("📱 Mobil Dasturlash (Flutter) - 9 oy"), callback_data="course_flutter"),
    ],
    [
        InlineKeyboardButton(text=_("🎥 Mobilografiya Kursi (2 oy)"), callback_data="course_mobilo"),
        InlineKeyboardButton(text=_("📊 Matematika Kursi"), callback_data="course_math"),
    ],
    [
        InlineKeyboardButton(text=_("🕌 Arab Tili Kursi"), callback_data="course_arabic"),
        InlineKeyboardButton(text=_("🇩🇪 Nemis Tili Kursi (0 dan B1 darajagacha)"), callback_data="course_german"),
    ],
    [
        InlineKeyboardButton(text=_("🇷🇺 Rus Tili Kursi (0 dan B1 darajagacha)"), callback_data="course_russian"),
        InlineKeyboardButton(text=_("🇬🇧 Ingliz Tili Kursi (0 dan B1 darajagacha)"), callback_data="course_english"),
    ],
    [
        InlineKeyboardButton(text=_("🌍 Xalqaro IELTS Kursi"), callback_data="course_ielts"),
    ],
    [
        InlineKeyboardButton(text=_("🔙 Ortga"), callback_data="go_back")
    ]
])