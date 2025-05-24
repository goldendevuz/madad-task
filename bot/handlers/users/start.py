from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from django.utils.translation import gettext as _
from icecream import ic

from bot.cruds.create import create_user
from bot.keyboards.reply.buttons import command_start
from bot.utils import with_user_language, update_google_sheet
from bot.utils.set_bot_commands import set_default_commands
from bot.utils.utils import format_as_html

if TYPE_CHECKING:
    from aiogram.types import Message

router = Router()

@router.message(CommandStart())
@router.message(CommandStart(deep_link=True))
@with_user_language
async def start_handler(message: Message, command: CommandStart):
    payload = command.args  # None if no deep link
    # if payload == "qobiliyat_testi":
        # await message.answer(f"👋 Welcome with deep link: <b>{payload}</b>")
        # Handle specific logic here
        # html_message = format_as_html(row)
        # async_to_sync(send_telegram_message)(html_message, phone=row[15])
        # await message.answer(html_message)
    # else:
        # await message.answer("👋 Welcome! No deep link detected.")
    # ic()
    from bot.loader import bot
    await set_default_commands(bot)
    # ic()

    user_data = await create_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        name=message.from_user.full_name,
        deep_link=payload,
    )
    # ic()

    if not user_data["is_user_created"]:
        # ic()
        text = _("Salom, {name}!\nSizni qayta ko'rib turganimizdan xursandmiz!").format(
            name=message.from_user.full_name
        )
        await message.answer(text, reply_markup=command_start)
    else:
        # ic()
        text = _("Xush kelibsiz, {name}!\n").format(name=message.from_user.full_name)
        await message.answer(text)
        await update_google_sheet()
