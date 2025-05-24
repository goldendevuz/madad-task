import json

import requests
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from icecream import ic
from rest_framework import generics
from rest_framework.decorators import api_view

from bot.utils.google import get_user_rows
from bot.utils.utils import format_as_html
from core.config import BASIC_AUTH_TOKEN
from .models import BotUser, Feedback
from .serializers import BotUserSerializer, FeedbackSerializer
from .webhook import proceed_update

User = get_user_model()


def home_view(request):
    # This view returns a simple HttpResponse
    return HttpResponse("<h1>Welcome to the Home Page!</h1>")


class BotUserAPIView(generics.ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer


class FeedbackAPIView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


def get_bot_user(request, user_id):
    try:
        user = BotUser.objects.get(user_id=user_id)
        return JsonResponse({"user_id": user.user_id,
                             "username": user.username,
                             "name": user.name,
                             "user_info": "User already exists"}, status=200)
    except BotUser.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)


# Register webhook
@csrf_exempt
async def telegram_webhook(request: HttpRequest):
    try:
        # Directly call the async function since we're in an async view
        await proceed_update(request)
    except Exception as e:
        # Log the exception
        ic(f"Error in webhook: {e}")
    return JsonResponse({"status": "ok"}, status=200)


SHEET_ID = '1TQJiyNvJXaMbQvvweNO9Yeg6VuybdmeSycMtSM5VkyE'


async def send_telegram_message(html_message, phone):
    pass


async def send_sms_message(html_message, phone):
    url = "https://piglet-factual-mentally.ngrok-free.app/api/sms/"

    payload = json.dumps({
        "number": phone.replace("+998", ""),
        "text": f"""{html_message}""",
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {BASIC_AUTH_TOKEN}',
    }
    ic(payload)
    ic(headers)

    response = requests.request("POST", url, headers=headers, data=payload)
    ic(response)
    ic(response.json())
    return response.json()


@api_view(['POST'])
def send_latest_google_response(request):
    rows = get_user_rows(SHEET_ID)
    ic(rows)
    if not rows:
        return JsonResponse({'status': 'error', 'message': 'No data found'})

    # user = User.objects.create(
    #     submitted_at=row[0],
    #     phone=row[15],
    # )
    # user.save()
    row = rows[-1]
    ic(row)
    # Check if the row is empty
    html_message = format_as_html(row)

    async_to_sync(send_sms_message)(html_message, phone=row[15])
    return JsonResponse({'status': 'sent', 'message': html_message})
