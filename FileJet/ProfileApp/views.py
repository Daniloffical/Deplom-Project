from django.shortcuts import render, redirect
from .models import Profile
from FileApp.models import File, Message, Chat
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError

from smtplib import SMTPSenderRefused

# Create your views here.

@login_required(login_url='main')
def show_profile(request):
    context = {}
    files = list(File.objects.filter(user = request.user))
    profile = Profile.objects.get(user=request.user)
    context['profile'] = profile
    context['files'] = files
    context['file_amount'] = len(files)


    chats_to_you = Chat.objects.filter(receive_user = request.user)

    messages_to_profile = []
   
    try:
        for chat in chats_to_you:
            message_to_profile = Message.objects.filter(chat = chat).order_by('pk').latest('pk')
            message_to_profile_user = message_to_profile.user
            file = chat.file

            message = message_to_profile.message

            if len(message) > 30:
                message = message[:30] + "..."
            else:
                message = message

            message = f"{chat.name} {message_to_profile_user.username}: {message}"

            message_to_profile_user_list = [file, message]
            messages_to_profile.append(message_to_profile_user_list)

        context['messages_to_profile'] = messages_to_profile
    except Message.DoesNotExist:
        pass

    chats_by_you = Chat.objects.filter(send_user = request.user)
    
    messages_by_profile = []

    try:
        for chat in chats_by_you:
            message_by_profile = Message.objects.filter(chat = chat).order_by('pk').latest('pk')
            message_by_profile_user = message_by_profile.user
            file = chat.file

            message = message_by_profile.message

            if len(message) > 30:
                message = message[:30] + "..."
            else:
                message = message


            message = f"{chat.name} {message_by_profile_user.username}: {message}"

            message_by_profile_user_list = [file, message]
            messages_by_profile.append(message_by_profile_user_list)

        context['messages_by_profile'] = messages_by_profile
    except Message.DoesNotExist:
        pass

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
        profile = Profile.objects.get(user=request.user)
        profile.authorised = True
        profile.save()
    except BadHeaderError:
        context['error'] = 'Знайдено некоректний заголовок'
    except SMTPSenderRefused:
        context['error'] = 'Неіснуюча пошта'
        profile = Profile.objects.get(user=request.user)
        profile.authorised = True
        profile.save()
    return redirect("profile")

@login_required(login_url='main')
def show_password_change(request):
    context = {}
    if request.method == 'POST':
        password = request.POST.get("password")
        password_confirm = request.POST.get("password-confirm")
        if password == password_confirm:
            user = request.user
            if not user.check_password(password):
                user.set_password(password)
                user.save()
                return redirect('main')
            else:
                context['error'] = 'Не можна використовувати існуючий пароль!'
        else:
            context['error'] = 'Паролі не співпадають'
    return render(request, 'password_change.html', context)