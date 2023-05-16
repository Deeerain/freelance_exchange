from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView
from django.contrib.auth import get_user_model, authenticate, login

from .models import Account
from .forms import LoginForm


class HomeView(TemplateView):
    template_name = 'burse/index.html'

class Freelancers(ListView):
    model = Account
    template_name = 'freelancers/list.html'


class LoginView(View):

    def get(self, request):
        form = LoginForm()

        return render(request, 'auth/login.html', {
            'form': form
        })
    
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            user = get_object_or_404(get_user_model(), username=form.cleaned_data['username'])
            if user.check_password(form.cleaned_data['password']):
                login(request, user)
                return redirect('tasks:list')
        
        return render(request, 'auth/login.html', {
            'form': form
        })