from django.urls import path

from auth_service.views import index

app_name = 'auth_service'
urlpatterns = [
    path('', index, name='index'),
]
