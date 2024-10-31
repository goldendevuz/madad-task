from django.contrib import admin
from django.urls import path, include
from webhook.views import home_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/webhook/', include('webhook.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)