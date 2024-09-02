from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

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


@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        return redirect('register')  # 탈퇴 후 회원가입 페이지로 리다이렉트
    return render(request, 'delete_account.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # 수정 후 홈 페이지로 리다이렉트
    else:
        form = UserUpdateForm(instance=request.user)
        
    return render(request, 'update_profile.html', {'form': form})