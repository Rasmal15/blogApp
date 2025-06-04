from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import *

# Register your models here.

class RegisteredUserAdmin(UserAdmin):
    # List of fields to display in the user change list page
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_staff', 'is_active')
    
    # Fields to be used in the search bar
    search_fields = ('username', 'email', 'phone')
    
    # Fields that can be filtered in the user list view
    list_filter = ('is_staff', 'is_active')
    
    # Fields to show in the user details page
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Add custom user creation form with additional fields
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone'),
        }),
    )

# Register your models here.
admin.site.register(UserProfile, RegisteredUserAdmin)