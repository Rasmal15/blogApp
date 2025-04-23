from django.contrib import admin
from .models import Posts

# Register your models here.

class AdminPostModel(admin.ModelAdmin):
    list_display = ('user','post','description','created_at','updated_at')
    
    list_filter = ('user','description','created_at')
    
    search_fields = ['description']
    

admin.site.register(Posts,AdminPostModel)