from django.shortcuts import render


def index(request):
    return render(request, 'auth_service/login.html')
