from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from app.forms import UserDataForm
from app.models import UserData


class UserDataCreateView(CreateView):
    """view страницы с формой для ввода информации о бизнесе"""
    
    model = UserData
    template_name = 'app/form.html'
    form_class = UserDataForm
    success_url = reverse_lazy('app:index')
    
    def form_valid(self, form):
        """При успешной валидации происходит редирект на страницу с данными"""
        business_name = form.cleaned_data.get('name')
        form = super().form_valid(form)
        return redirect('app:info', business_name)
    
    
def show_business_helpers(request, business_name):
    """view страницы со сгенерированными ИИ данными"""
    
    template = 'app/info.html'
    return render(request, template)