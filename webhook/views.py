from django.http import HttpResponse, HttpRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from .models import BotUser, Feedback
from .serializers import BotUserSerializer, FeedbackSerializer
from .webhook import proceed_update


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
        print(f"Error in webhook: {e}")
    return JsonResponse({"status": "ok"}, status=200)
