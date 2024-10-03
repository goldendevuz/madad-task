import json
from aiogram import types, Bot, Dispatcher
from aiogram.types import Update
from django.http import HttpRequest, HttpResponse
from bot.loader import bot, dp


async def proceed_update(req: HttpRequest):
    upd = types.Update(**(json.loads(req.body)))
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp._process_update(bot, upd)


# async def proceed_update(request_body):
#     update = Update.parse_raw(request_body)  # Parse the raw request body into an Update object
#     await dp.process_update(update)  # Correct method to handle updates in aiogram 3