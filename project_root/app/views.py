from django.shortcuts import render


def index(request):
    template = 'app/form.html'
    return render(request, template)
