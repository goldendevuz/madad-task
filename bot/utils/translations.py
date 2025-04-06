from functools import wraps
from django.utils.translation import activate
from asgiref.sync import sync_to_async
from webhook.models import BotUser  # Replace with your actual app name

@sync_to_async
def get_user_language(user_id):
    try:
        user = BotUser.objects.get(user_id=user_id)
        return user.language or "uz"
    except BotUser.DoesNotExist:
        return "uz"

def with_user_language(func):
    @wraps(func)
    async def wrapper(message, *args, **kwargs):
        user_id = message.from_user.id
        lang = await get_user_language(user_id)
        activate(lang)
        return await func(message, *args, **kwargs)
    return wrapper