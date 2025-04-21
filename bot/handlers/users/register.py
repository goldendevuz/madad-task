from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from django.utils.translation import gettext as _

from bot.keyboards.reply.buttons import registration_keyboard, contact_request_keyboard
from bot.states import RegistrationStates

router = Router()

# Ro'yxatdan o'tish bosqichi boshlanishi: foydalanuvchi "Ro'yxatdan o'tish" tugmasini bosadi
@router.message(F.text == _("📝 Ro'yxatdan o'tish"))
async def start_registration(message: Message, state: FSMContext):
    await message.answer("Iltimos, ismingizni kiriting:")
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

# Foydalanuvchidan telefon raqamini so'ralmoqda
@router.message(RegistrationStates.phone)
async def process_phone(message: Message, state: FSMContext):
    # Agar foydalanuvchi tugma orqali yuborgan bo‘lsa
    if message.contact:
        phone = message.contact.phone_number
    else:
        # Qo‘lda yozgan bo‘lsa
        phone = message.text

    await state.update_data(phone=phone)
    await message.answer(
        "Qaysi kursga yozilmoqchisiz? Quyidagi variantlardan birini tanlang:",
        reply_markup=registration_keyboard()
    )
    await state.set_state(RegistrationStates.course)

# Foydalanuvchidan kurs tanlovini so'ralmoqda
@router.message(RegistrationStates.course)
async def process_course(message: Message, state: FSMContext):
    await state.update_data(course=message.text)
    user_data = await state.get_data()
    confirmation_text = (
        "Quyidagi ma'lumotlar qabul qilindi:\n"
        f"Ism: {user_data.get('name')}\n"
        f"Telefon: {user_data.get('phone')}\n"
        f"Kurs: {user_data.get('course')}\n\n"
        "Ma'lumotlaringiz uchun rahmat!"
    )
    await message.answer(confirmation_text)
    # Shu yerda ma'lumotlarni ma'lumotlar bazasiga yoki jadval tizimiga saqlash kodini joylashtiring.
    await state.clear()
