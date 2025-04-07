from aiogram import Router, types
from aiogram.filters.command import Command

from core.data.config import ADMINS

router = Router()


@router.message(Command('help'))
async def bot_help(message: types.Message):
    # Check if the user is an admin
    if str(message.from_user.id) in ADMINS:
        # Admin help message
        text = ("Buyruqlar: ",
                "/start - Botni ishga tushirish",
                "/help - Yordam",
                "/allusers - Foydalanuvchilar ro'yxatini ko'rish",
                "/reklama - Reklama yuborish")
    else:
        # Default help message for non-admins
        text = ("Buyruqlar: ",
                "/start - Botni ishga tushirish",
                "/help - Yordam")
    await message.answer(text="\n".join(text))
