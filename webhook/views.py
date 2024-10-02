from .models import BotUser
from django.http import HttpResponse, HttpRequest   
from asgiref.sync import async_to_sync
from .webhook import proceed_update
from .serializers import BotUserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics


# Create your views here.
class BotUserAPIView(generics.ListCreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer

@csrf_exempt
def telegram(request: HttpRequest):
    try:
        async_to_sync(proceed_update)(request)
    except Exception as e:
        print(e)
    return HttpResponse()
