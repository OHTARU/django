from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def register(request):
    if request.method == 'POST':
        user_forms = RegisterForm(request.POST)
        if user_forms.is_valid():
            user_forms.save()
            return redirect('login')
    else:
        user_forms = RegisterForm()
        
    return render(request, 'register.html', {'form': user_forms})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')