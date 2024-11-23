from django.contrib import admin

from app.models import DataFromSite, GeneratedData,  UserData


@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    """Класс регистрации модели UserData в admin-панели"""
    
    list_display = ['name', 'business_type', 'region', 'industry', 'is_innovative']
    list_display_links = ['name']
    

@admin.register(DataFromSite)
class DataFromSite(admin.ModelAdmin):
    """Класс регистрации модели DataFromSite в admin-панели"""
    
    list_display = [
        'id',
        'site_url',
        ]
    list_display_links = [
        'id'
    ]
    
    
@admin.register(GeneratedData)
class GeneratedDataAdmin(admin.ModelAdmin):
    """Класс регистрации модели GeneratedData в admin-модели"""
    
    list_display = [
        'id',
        'user_data__name',
    ]
    list_display_links = [
        'id',
    ]
    raw_id_fields = [
        'user_data',
    ]
    