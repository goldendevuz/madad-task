from .models import BotUser
import asyncio
from django.http import HttpResponse, HttpRequest   
from .webhook import proceed_update
from .serializers import BotUserSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

def home_view(request):
    # This view returns a simple HttpResponse
    return HttpResponse("<h1>Welcome to the Home Page!</h1>")

# Create your views here.
class BotUserAPIView(generics.ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer




@csrf_exempt
async def telegram_webhook(request: HttpRequest):
    try:
        # Directly call the async function since we're in an async view
        await proceed_update(request)
    except Exception as e:
        # Log the exception
        print(f"Error in webhook: {e}")
    return JsonResponse({"status": "ok"}, status=200)
