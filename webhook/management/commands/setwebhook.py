from asgiref.sync import async_to_sync
from django.core.management.base import BaseCommand

from bot.loader import bot
from core.data.config import WEBHOOK_URL


class Command(BaseCommand):
    help = 'Setting webhook'

    async def set_webhook_async(self):
        async with bot:
            webhook = await bot.get_webhook_info()
            if webhook.url != WEBHOOK_URL:
                await bot.set_webhook(WEBHOOK_URL)
                self.stdout.write(self.style.NOTICE(f"Webhook url: {WEBHOOK_URL}"))
                self.stdout.write(self.style.SUCCESS("Webhook set successfully!"))
            else:
                self.stdout.write(self.style.NOTICE(f"Webhook url: {WEBHOOK_URL}"))
                self.stdout.write(self.style.WARNING("Webhook is already setted!"))

    def handle(self, *args, **kwargs):
        async_to_sync(self.set_webhook_async)()
