from django.contrib import admin

from app.models import UserData


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'business_type', 'region', 'industry', 'is_innovative']
    list_display_links = ['name']
    
