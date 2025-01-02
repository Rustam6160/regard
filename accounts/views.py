from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', context={'form': form})


@login_required
def dashboard(request):
    return render(request, 'accounts/profile.html')



def custom_logout(request):
    logout(request)
    return redirect('login')  # Перенаправляем на страницу входа

