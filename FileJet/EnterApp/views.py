from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from ProfileApp.models import Profile
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login




# Create your views here.
def show_login(request):
    context = {}
    if request.method == 'POST':
        user_login = request.POST.get("login")
        password = request.POST.get("password")
        user = authenticate(request, username = user_login, password = password)
        if user != None:
            login(request, user)
            return redirect('main')
        else:
            context['error'] = 'Невірний логін'
    return render(request, 'login.html', context)

def show_registration(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        login = request.POST.get('login')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        context['name'] = name
        context['login'] = login
        context['email'] = email
        context['password'] = password
        context['password_confirm'] = password_confirm
        if password == password_confirm:
            try:
                user = User.objects.create_user(username = login, password = password, email=email, first_name = name)
                Profile.objects.create(user=user)
                return redirect('login')
            except IntegrityError:
                context['error'] = 'Користувач вже існує'
        else:
            context['error'] = 'Паролі не співпадаються'
    return render(request, 'registration.html', context)