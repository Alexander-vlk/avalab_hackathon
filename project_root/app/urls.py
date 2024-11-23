from django.urls import path

from app.views import index, UserDataCreateView

app_name = 'app'
urlpatterns = [
    path('', UserDataCreateView.as_view(), name='index'),
]
