from __future__ import annotations
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from bot.keyboards.reply.buttons import main_menu
from bot.keyboards.inline.buttons import inline_menu
from bot.utils.set_bot_commands import set_default_commands
from typing import TYPE_CHECKING
from aiogram import Router
from bot.loader import bot
from bot.cruds.create import create_user
from django.utils.translation import activate, gettext as _
from asgiref.sync import sync_to_async  # sync call (usually very fast)
from webhook.models import BotUser
from bot.utils import with_user_language

if TYPE_CHECKING:
    from aiogram.types import Message

router = Router()


@router.message(CommandStart())
@with_user_language
async def command_start_handler(message: Message):
    await set_default_commands(bot)

    user_data = await create_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        name=message.from_user.full_name
    )

    if not user_data["is_user_created"]:
        text = _("Salom, {name}!\nSizni qayta ko'rib turganimizdan xursandmiz!").format(
            name=message.from_user.full_name
        )
        await message.answer(text, reply_markup=inline_menu)
    else:
        text = _("Xush kelibsiz, {name}!\n").format(name=message.from_user.full_name)
        await message.answer(text, reply_markup=main_menu)


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
    # await callback_query.answer()
    await callback_query.message.edit_reply_markup(reply_markup=None)