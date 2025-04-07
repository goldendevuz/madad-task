import asyncio

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message
from django.utils.translation import gettext as _


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, slow_mode_delay=0.5):
        super().__init__()
        self.user_timeouts = {}
        self.slow_mode_delay = slow_mode_delay

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        current_time = asyncio.get_event_loop().time()  # Use asyncio's time for non-blocking
        last_request_time = self.user_timeouts.get(user_id, 0)

        if current_time - last_request_time < self.slow_mode_delay:
            # Send a rate-limit warning if requests are too frequent
            await event.reply(_("Juda ko'p so'rov! Biroz kuting."))
            return
        else:
            # Update the last request time and clean up old entries if needed
            self.user_timeouts[user_id] = current_time
            # Pass the event to the next handler
            return await handler(event, data)
