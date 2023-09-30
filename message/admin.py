from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display=("body","is_read","timestamp")
admin.site.register(Message,MessageAdmin)    
