from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from django.utils.translation import gettext as _

from bot.keyboards.inline.buttons import courses_keyboard

router = Router()

# Title as a separate variable
COURSE_TITLE = _("💻 Kompyuter Savodxonligi PRO")


# Inline buttons for the course details
def course_inline_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=_("📚 Kurs mazmuni"), callback_data="course_content"),
                InlineKeyboardButton(text=_("🧠 Olinadigan ko‘nikmalar"), callback_data="skills"),
            ],
            [
                InlineKeyboardButton(text=_("👥 Kurs kimlar uchun?"), callback_data="audience"),
                InlineKeyboardButton(text=_("📚 Darslar formati"), callback_data="schedule"),
            ],
            [
                InlineKeyboardButton(text=_("💰 Kurs qiymati"), callback_data="price"),
                InlineKeyboardButton(text=_("💳 Muddatli to‘lov"), callback_data="payment"),
            ]
        ]
    )


@router.message(F.text == _("🎓 Kurslar haqida ma'lumot"))
async def feedback_1(message: Message):
    await message.reply(
        _("Kurslardan birini tanlang 👇"), reply_markup=courses_keyboard
    )


# Initial message with title and body content
@router.message(F.text == _("💻 Kompyuter Savodxonligi PRO"))
async def send_course_details(message: Message):
    await message.answer(
        _(
            "{course_title}\n\n"
            "<b>📚 Kurs mazmuni:</b>\n"
            "🔹 Kompyuter tizimlarining ishlash prinsiplari\n"
            "🔹 Microsoft Office (Word, Excel, PowerPoint)\n"
            "🔹 Google Workspace (Docs, Sheets, Forms)\n"
            "🔹 Sun’iy intellekt vositalari va ularni ofis dasturlari bilan integratsiya qilish\n\n"
            "<b>👨‍🏫 Ustoz:</b> Abdulaziz Abdullayev — xalqaro sertifikatga ega tajribali mutaxassis\n\n"
            "<b>📌 Sizga qaysi bo‘limni ko‘rishni xohlaysiz?</b>\n"
            "⚙️ <b>Tanlang:</b> Kerakli bo‘limni tugmalar yordamida tanlang.\n"
        ).format(course_title=COURSE_TITLE),
        reply_markup=course_inline_keyboard()
    )


@router.callback_query(F.data == "instructor")
async def show_instructor(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        _(
            "{course_title}\n\n"
            "<b>👨‍🏫 Ustoz:</b> Abdulaziz Abdullayev — xalqaro sertifikatga ega tajribali mutaxassis\n\n"
            "<b>📌 Sizga qaysi bo‘limni ko‘rishni xohlaysiz?</b>\n"
            "⚙️ <b>Tanlang:</b> Kerakli bo‘limni tugmalar yordamida tanlang."
        ).format(course_title=COURSE_TITLE),
        reply_markup=course_inline_keyboard()  # Keeping buttons intact
    )


@router.callback_query(F.data == "skills")
async def show_skills(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        _(
            "{course_title}\n\n"
            "<b>🛠 Olinadigan ko‘nikmalar:</b>\n"
            "✔ Hisobot va hujjatlarni avtomatlashtirish\n"
            "✔ Ma’lumotlar bazasi bilan ishlash\n"
            "✔ Ofis dasturlaridan samarali foydalanish\n"
            "✔ Sun’iy intellekt texnologiyalarini amaliyotda qo‘llash\n\n"
            "<b>📌 Sizga qaysi bo‘limni ko‘rishni xohlaysiz?</b>\n"
            "⚙️ <b>Tanlang:</b> Kerakli bo‘limni tugmalar yordamida tanlang."
        ).format(course_title=COURSE_TITLE),
        reply_markup=course_inline_keyboard()  # Keeping buttons intact
    )


@router.callback_query(F.data == "audience")
async def show_audience(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        _(
            "{course_title}\n\n"
            "👥 <b>Kurs kimlar uchun?</b>\n"
            "✅ <b>Biznes egalari va tadbirkorlar:</b> AI va avtomatlashtirish orqali unumdorlikni oshirish\n"
            "✅ <b>Ofis xodimlari va menejerlar:</b> Office, Google Workspace va AI bilan samarali ishlash\n"
            "✅ <b>Talabalar va yangi ish boshlaganlar:</b> Ishga joylashish imkoniyatlarini oshirish\n"
            "✅ <b>Frilanserlar:</b> Texnik ko‘nikmalarni mustahkamlash, mijozlar sonini ko‘paytirish\n\n"
            "<b>📌 Sizga qaysi bo‘limni ko‘rishni xohlaysiz?</b>\n"
            "⚙️ <b>Tanlang:</b> Kerakli bo‘limni tugmalar yordamida tanlang."
        ).format(course_title=COURSE_TITLE),
        reply_markup=course_inline_keyboard()
    )


@router.callback_query(F.data == "schedule")
async def show_schedule(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        _(
            "{course_title}\n\n"
            "<b>📅 Darslar formati:</b>\n"
            "✅ Standart: oflayn | 3 oy | haftada 3 kun | har biri 2 soat\n"
            "✅ Bootcamp: oflayn | 2 oy | haftada 5 kun | har biri 2 soat\n\n"
            "<b>📌 Sizga qaysi bo‘limni ko‘rishni xohlaysiz?</b>\n"
            "⚙️ <b>Tanlang:</b> Kerakli bo‘limni tugmalar yordamida tanlang."
        ).format(course_title=COURSE_TITLE),
        reply_markup=course_inline_keyboard()  # Keeping buttons intact
    )


@router.callback_query(F.data == "price")
async def show_price(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        _(
            "{course_title}\n\n"
            "<b>💰 Kurs qiymati:</b>\n"
            "• Standart: 1 oylik - <b>575 000 so‘m</b>\n"
            "• Bootcamp: 1 oylik - <b>900 000 so‘m</b>\n\n"
            "<b>📌 Sizga qaysi bo‘limni ko‘rishni xohlaysiz?</b>\n"
            "⚙️ <b>Tanlang:</b> Kerakli bo‘limni tugmalar yordamida tanlang."
        ).format(course_title=COURSE_TITLE),
        reply_markup=course_inline_keyboard()  # Keeping buttons intact
    )


@router.callback_query(F.data == "payment")
async def show_payment(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        _(
            "{course_title}\n\n"
            "💳 <b>Muddatli to‘lov:</b>\n"
            "Kurs uchun to‘lovni muddatli to‘lovga o‘tkazish mumkin.\n"
            "Qo‘shimcha ma’lumot olish uchun biz bilan bog‘laning.\n\n"
            "<b>📌 Sizga qaysi bo‘limni ko‘rishni xohlaysiz?</b>\n"
            "⚙️ <b>Tanlang:</b> Kerakli bo‘limni tugmalar yordamida tanlang."
        ).format(course_title=COURSE_TITLE),
        reply_markup=course_inline_keyboard()
    )


@router.callback_query(F.data == "course_content")
async def show_course_content(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        _(
            "{course_title}\n\n"
            "<b>📚 Kurs mazmuni:</b>\n"
            "🔹 Kompyuter tizimlarining ishlash prinsiplari\n"
            "🔹 Microsoft Office (Word, Excel, PowerPoint)\n"
            "🔹 Google Workspace (Docs, Sheets, Forms)\n"
            "🔹 Sun’iy intellekt vositalari va ularni ofis dasturlari bilan integratsiya qilish\n\n"
            "<b>📌 Sizga qaysi bo‘limni ko‘rishni xohlaysiz?</b>\n"
            "⚙️ <b>Tanlang:</b> Kerakli bo‘limni tugmalar yordamida tanlang."
        ).format(course_title=COURSE_TITLE),
        reply_markup=course_inline_keyboard()  # Keeping buttons intact
    )
