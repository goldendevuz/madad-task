from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.methods.set_my_commands import BotCommand
from aiogram.types import BotCommandScopeDefault, BotCommandScopeChat
from icecream import ic

from core.config import ADMINS


# ic(ADMINS)


async def set_default_commands(bot: Bot):
    # Commands for everyone
    default_commands = [
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/help", description="Yordam"),
        BotCommand(command="/setlang", description="Set bot language"),
    ]
    await bot.set_my_commands(commands=default_commands, scope=BotCommandScopeDefault())

    # Commands for administrators
    admin_commands = default_commands + [
        BotCommand(command="/allusers", description="Get all users"),
        BotCommand(command="/advertising", description="Give advertising post"),

        # BotCommand(command="ban", description="Ban a user"),
        # BotCommand(command="unban", description="Unban a user"),
    ]

    for admin in ADMINS:
        try:
            await bot.set_my_commands(commands=admin_commands, scope=BotCommandScopeChat(chat_id=admin))
        except TelegramBadRequest as e:
            return e
            # ic(e, admin)
