from django.shortcuts import render
from django.views.generic.edit import CreateView

from app.forms import UserDataForm
from app.models import UserData



def index(request):
    template = 'app/form.html'
    return render(request, template)


class UserDataCreateView(CreateView):
    model = UserData
    template_name = 'app/form.html'
    form_class = UserDataForm
    