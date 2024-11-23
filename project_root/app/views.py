from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from app.forms import UserDataForm
from app.models import UserData



def index(request, business_name):
    template = 'app/info.html'
    return render(request, template)


class UserDataCreateView(CreateView):
    model = UserData
    template_name = 'app/form.html'
    form_class = UserDataForm
    success_url = reverse_lazy('app:index')
    
    def form_valid(self, form):
        business_name = form.cleaned_data.get('name')
        form = super().form_valid(form)
        return redirect('app:info', business_name)
    
    