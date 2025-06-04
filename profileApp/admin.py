from django.contrib import admin
from . models import ProfileData



# Register your models here.

class RegisteredUserProfile(admin.ModelAdmin):
    list_display = ('user','name','profile_picture')
    
    search_fields = ['name']
    

admin.site.register(ProfileData,RegisteredUserProfile)