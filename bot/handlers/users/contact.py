from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from django.utils.translation import gettext as _

from bot.keyboards.inline.buttons import contact_inline_keyboard

router = Router()

@router.message(F.text == _("📞 Bog'lanish"))
async def send_contact_info(message: Message):
    contact_text = (
        "🏢 Bizning manzil:\n"
        "Qo'qon sh. Usmon Nosir 28A\n\n"
        "☎️ Telefon:\n"
        "+998 99 600 77 07\n"
        "+998 33 600 77 07\n\n"
        "✉️ Email:\n"
        "madad.talim@gmail.com\n\n"
    )
    # "Bog'lanish" sarlavhasi uchun ham icon qo'shamiz
    await message.answer(contact_text, reply_markup=contact_inline_keyboard())