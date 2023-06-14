from django.shortcuts import render, redirect
from .models import Profile
from FileApp.models import File
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError


# Create your views here.

@login_required(login_url='main')
def show_profile(request):
    context = {}
    files = list(File.objects.filter(user = request.user))
    profile = Profile.objects.get(user=request.user)
    context['profile'] = profile
    context['files'] = files
    print(files)
    return render(request, 'profile.html', context)

@login_required(login_url='main')
def log_out(request):
    logout(request)
    return redirect("main")

@login_required(login_url='main')
def authenticate(request):
    context = {}
    user_mail = request.user.email
    user_name = request.user.username
    message = f"Вітаю: {user_name}\nВи підтвердили вашу пошту на сайті FileJet\nhttps://127.0.0.1:8000"
    try:
        send_mail('Тема', message, 'settings.EMAIL_HOST_USER', [user_mail]) 
    except BadHeaderError:
        context['error'] = 'Знайдено некоректний заголовок'
    return redirect("profile")

