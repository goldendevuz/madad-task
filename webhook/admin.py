from django.contrib import admin
from .models import BotUser

admin.site.site_header = "Pipcoder admin"  # Title displayed at the top of the admin page
admin.site.site_title = "@pipcoder"    # Title displayed in the browser tab
admin.site.index_title = "Webhook bot"  # Title displayed on the admin index page

class BaseAdmin(admin.ModelAdmin):
    list_per_page = 10

    class Meta:
        abstract = True

# Register your models here.
@admin.register(BotUser)
class BotUserAdmin(BaseAdmin):
    list_display = [f.name for f in BotUser._meta.fields]
    search_fields = ('user_id', 'username', 'name')