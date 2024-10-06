from __future__ import annotations
from aiogram.filters import CommandStart
from aiogram.types import Message
# from typing import TYPE_CHECKING

from aiogram import Router
from aiogram.filters import Command

# from api.user.models import User

# if TYPE_CHECKING:
    # from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}!")

@router.message(Command(commands=["id"]))
async def handle_id_command(message: Message) -> None:
    if message.from_user is None:
        return

    await message.answer(f"User Id: <b>{message.from_user.id}</b>\nChat Id: <b>{message.chat.id}</b>")