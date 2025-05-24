import re
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from django.utils.translation import gettext as _
from decouple import config

from bot.keyboards.reply.buttons import registration_keyboard, contact_request_keyboard
from bot.states import RegistrationStates

router = Router()

# Ro'yxatdan o'tish bosqichi boshlanishi: foydalanuvchi "Ro'yxatdan o'tish" tugmasini bosadi
@router.message(F.text == _("📝 Ro'yxatdan o'tish"))
async def start_registration(message: Message, state: FSMContext):
    await message.answer("Ism sharifingizni kiriting:")
    await state.set_state(RegistrationStates.name)

# Foydalanuvchidan ism so'ralmoqda
@router.message(RegistrationStates.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(
        "Telefon raqamingizni yuboring:",
        reply_markup=contact_request_keyboard()
    )
    await state.set_state(RegistrationStates.phone)

@router.message(RegistrationStates.phone)
async def process_phone(message: Message, state: FSMContext):
    # Agar foydalanuvchi tugma orqali yuborgan bo‘lsa
    if message.contact:
        phone = message.contact.phone_number
    else:
        phone = message.text.strip()

    # Telefon raqamini +998 formatga keltirish
    if phone.startswith("998") and len(phone) == 12:
        phone = "+" + phone
    elif phone.startswith("9") and len(phone) == 9:
        phone = "+998" + phone

    # Telefon raqamini tekshirish
    if not re.fullmatch(r"\+998\d{9}", phone):
        await message.answer("Iltimos, telefon raqamingizni to'g'ri kiriting. Masalan: +998901234567 yoki 901234567")
        return

    await state.update_data(phone=phone)
    await message.answer(
        "Qaysi kursga yozilmoqchisiz? Quyidagi variantlardan birini tanlang:",
        reply_markup=registration_keyboard()
    )
    await state.set_state(RegistrationStates.course)

@router.message(RegistrationStates.course)
async def process_course(message: Message, state: FSMContext):
    await state.update_data(course=message.text)
    user_data = await state.get_data()
    confirmation_text = (
        "Quyidagi ma'lumotlar qabul qilindi:\n"
        f"Ism: {user_data.get('name')}\n"
        f"Telefon: {user_data.get('phone')}\n"
        f"Kurs: {user_data.get('course')}\n\n"
        "Sizning ma'lumotlaringiz qabul qilindi, operator javobini kuting!"
    )

    # Send to user
    await message.answer(confirmation_text)
    from bot.loader import bot

    # Send to each admin
    for admin_id in config("ADMINS"):
        try:
            await bot.send_message(chat_id=admin_id, text=confirmation_text)
        except Exception as e:
            print(f"Failed to send message to admin {admin_id}: {e}")

    # Optionally save to DB here
    await state.clear()

