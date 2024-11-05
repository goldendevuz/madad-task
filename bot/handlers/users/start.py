from __future__ import annotations
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from bot.keyboards.reply.buttons import main_menu
from bot.keyboards.inline.buttons import inline_menu
from typing import TYPE_CHECKING
from aiogram import Router
from bot.db.create import create_user

if TYPE_CHECKING:
    from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user = await create_user(user_id=message.from_user.id, 
                                  username=message.from_user.username, 
                                  name=message.from_user.full_name)
    # user={"is_user_created":False}
    if user["is_user_created"]==False:
        await message.answer(f"Salom, {message.from_user.full_name}!\nSizni qayta ko'rib turganimizdan xursandmiz!",reply_markup=inline_menu)  
    else:
        await message.answer(f"Xush kelibsiz, {message.from_user.full_name}!\n", reply_markup=main_menu)

# Handle Yes/No responses from reply keyboard
@router.message(lambda message: message.text in ["✅ Yes", "❌ No"])
async def process_reply(message: Message):
    if message.text == "✅ Yes":
        await message.answer("You selected ✅ Yes. Proceeding...", reply_markup=ReplyKeyboardRemove())
        # Add any action for "Yes" here
    elif message.text == "❌ No":
        await message.answer("You selected ❌ No. Stopping...", reply_markup=ReplyKeyboardRemove())
        # Stop action logic here if needed


# Callback handler for Yes and No inline buttons
@router.callback_query(lambda c: c.data in ['yes', 'no'])
async def process_callback(callback_query: CallbackQuery):
    if callback_query.data == 'yes':
        await callback_query.message.answer("You selected ✅ Yes. Proceeding...")
        # Add any action for "Yes" here
    elif callback_query.data == 'no':
        await callback_query.message.answer("You selected ❌ No. Stopping...")
        # Stop action logic here if needed

    # Answer callback to remove "loading" animation on buttons
    await callback_query.answer()