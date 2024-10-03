from .models import BotUser
from django.http import HttpResponse, HttpRequest   
from asgiref.sync import async_to_sync
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


# @csrf_exempt
# async def telegram_webhook(request):
#     if request.method == 'POST':
#         request_body = request.body.decode('utf-8')
#         await proceed_update(request_body)
#         return JsonResponse({"status": "ok"})
#     return JsonResponse({"status": "method not allowed"}, status=405)

@csrf_exempt
def telegram_webhook(request: HttpRequest):
    try:
        async_to_sync(proceed_update)(request)
        # print(request.body)
    except Exception as e:
        print(e)
    return HttpResponse("<h1>Welcome to the WEBHOOK Page!</h1>")
