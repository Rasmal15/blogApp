from django.contrib import admin
from .models import Comment

# Register your models here.

class CommentAdmin (admin.ModelAdmin):
    list_display = ('comment','user', 'post')
    
    list_filter = ('post'),
    
    search_fields = ('post', 'comment')
    
admin.site.register(Comment,CommentAdmin)