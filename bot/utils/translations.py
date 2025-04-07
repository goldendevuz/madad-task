from functools import wraps

from asgiref.sync import sync_to_async
from django.utils.translation import override

from webhook.models import BotUser


@sync_to_async
def get_user_language(user_id):
    try:
        user = BotUser.objects.get(user_id=user_id)
        result = user.language or "uz"
        return result
    except BotUser.DoesNotExist:
        return "uz"


def with_user_language(func):
    @wraps(func)
    async def wrapper(message, *args, **kwargs):
        user_id = message.from_user.id
        lang = await get_user_language(user_id)
        # ic("User language is:", lang)
        with override(lang):
            # ic("Activated lang in context:", lang)
            return await func(message, *args, **kwargs)

    return wrapper
