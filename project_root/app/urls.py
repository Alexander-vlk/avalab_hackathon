from django.urls import path

from app.views import show_business_helpers, UserDataCreateView

app_name = 'app'
urlpatterns = [
    path('', UserDataCreateView.as_view(), name='index'),
    path('info/<str:business_name>', show_business_helpers, name='info'),
]
