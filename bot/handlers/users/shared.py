from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.states import RegistrationStates
from django.utils.translation import gettext as _
from core.data.config import ADMINS

router = Router()

# @router.callback_query(lambda c: c.data == "go_back")
# async def handle_go_back(callback: CallbackQuery, state: FSMContext):
#     await callback.message.delete()  # xabarni o'chirish
#     await callback.answer()
#     await state.clear()

@router.callback_query(lambda c: c.data == "go_back")
async def handle_go_back(callback: CallbackQuery, state: FSMContext):
    try:
        await callback.message.delete()  # joriy xabarni o'chirish
        await callback.bot.delete_message(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id - 1  # oldingi xabarni o'chirish
        )
    except Exception as e:
        # agar xabar allaqachon o‘chirilgan yoki mavjud bo‘lmasa, xatolikni yutib yuboramiz
        print(f"Xabarni o‘chirishda xatolik: {e}")

    await callback.answer()
    await state.clear()
