from django.contrib import admin
from .models import BotUser

admin.site.site_header = "Pipcoder admin"  # Title displayed at the top of the admin page
admin.site.site_title = "@pipcoder"    # Title displayed in the browser tab
admin.site.index_title = "Webhook bot"  # Title displayed on the admin index page

# Register your models here.
@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'name', 'created_at')
    search_fields = ('user_id', 'username', 'name')