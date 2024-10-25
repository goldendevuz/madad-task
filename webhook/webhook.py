import json
from aiogram import types
from django.http import HttpRequest
from bot.loader import bot, dp


async def proceed_update(req: HttpRequest):
    print("Umrbek Webhook: ", req.body)
    upd = types.Update(**(json.loads(req.body)))
    await dp.feed_update(bot, upd)