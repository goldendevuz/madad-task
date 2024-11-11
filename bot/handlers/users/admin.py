from bot.utils.misc.logging import logging
import asyncio
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from bot.cruds.get_users import get_all_users
from bot.states.test import AdminState
from bot.filters.admin import IsBotAdminFilter
from core.data.config import ADMINS
from bot.utils.pgtoexcel import export_to_excel
from bot.keyboards.reply.buttons import cancel_kb

router = Router()


@router.message(Command('allusers'), IsBotAdminFilter(ADMINS))
async def get_users(message: types.Message):
    users = await get_all_users()
    file_path = f"bot/data/users.xlsx"
    if len(users) != 0:
        await export_to_excel(data=users, filepath=file_path)
        await message.answer_document(types.input_file.FSInputFile(file_path))
    else:
        await message.answer("Foydalanuvchilar bazada topilmadi")    


@router.message(Command('reklama'), IsBotAdminFilter(ADMINS))
async def ask_ad_content(message: types.Message, state: FSMContext):
    await message.answer("Reklama uchun post yuboring", reply_markup=cancel_kb)
    await state.set_state(AdminState.ask_ad_content)


@router.message(AdminState.ask_ad_content, IsBotAdminFilter(ADMINS))
async def send_ad_to_users(message: types.Message, state: FSMContext):
    #  Check if the message is "❌ Bekor qilish", if so, cancel ad and clear the state
    if message.text == "❌ Bekor qilish":
        await message.answer("Reklama bekor qilindi.", reply_markup=types.ReplyKeyboardRemove())
    else:
         # Send the ad to all users
        users = await get_all_users()
        count = 0
        for user in users:
            try:
                await message.send_copy(chat_id=user["user_id"])
                count += 1
                await asyncio.sleep(0.05)
            except Exception as error:
                logging.info(f"Add did not send to user: {user["user_id"]}. Error: {error}")
        await message.answer(text=f"Reklama {count} ta foydalauvchiga muvaffaqiyatli yuborildi.")
    await state.clear()
