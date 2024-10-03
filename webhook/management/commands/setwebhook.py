from django.core.management.base import BaseCommand
from bot.loader import bot
from core.settings import WEBHOOK_URL
import asyncio


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
        # Run the asynchronous function using asyncio
        asyncio.run(self.set_webhook_async())
