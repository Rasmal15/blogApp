from django.contrib import admin
from .models import ReplayComment

# Register your models here.

class ReplayAdmin(admin.ModelAdmin):
    list_display = ('replay','user', 'comment')
    
    list_filter = ('comment'),
    
    search_fields = ('comment', 'replay')
    
admin.site.register(ReplayComment,ReplayAdmin)