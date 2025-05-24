import hashlib
import os

from environs import Env
from icecream import ic

# todo:Open environs kutubxonasi orqali env faylidagi malumotlarni olamiz
env = Env()
# .env file ni core/data ichida ochamiz
if not os.path.exists('core/data/.env'):
    ic('.env fayli topilmadi!')
    ic('.env.example faylidan nusxa ko\'chirib shablonni o\'zizga moslang.')
    exit(1)
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMINS = env.list("ADMINS")
WEBHOOK_DOMAIN = env.str('WEBHOOK_DOMAIN')
SECRET_KEY = env.str('SECRET_KEY')
BASE_URL = env.str('BASE_URL')
DEBUG = env.bool('DEBUG')

# webhook url yasash uchun noyob path yaratamiz
# WEBHOOK_PATH = "webhook/" 
# yoki
WEBHOOK_PATH = hashlib.md5(BOT_TOKEN.encode()).hexdigest()
WEBHOOK_URL = f"{WEBHOOK_DOMAIN}/api/webhook/{WEBHOOK_PATH}"

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")
CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE", default=True)
DB_PATH = env.str("DB_PATH", default="db.sqlite3")
BASIC_AUTH_TOKEN=env.str("BASIC_AUTH_TOKEN")
