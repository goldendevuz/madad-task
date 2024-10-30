import os
from environs import Env

#todo:Open environs kutubxonasi orqali env faylidagi malumotlarni olamiz
env = Env()
if not os.path.exists('core/data/.env'):
    print('.env fayli topilmadi!')
    print('.env.example faylidan nusxa ko\'chirib shablonni o\'zizga moslang.')
    exit(1)
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMINS = env.list("ADMINS")
WEBHOOK_DOMAIN = env.str('WEBHOOK_DOMAIN')
SECRET_KEY = env.str('SECRET_KEY')
BASE_URL = env.str('BASE_URL')
DEBUG = env.bool('DEBUG')