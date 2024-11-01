from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from bot.handlers import setup_routers
# from utils.db.postgres import Database
from core.data.config import BOT_TOKEN
from bot.middlewares.throttling import ThrottlingMiddleware

# db = Database()
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
dp.include_router(setup_routers())
dp.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))

