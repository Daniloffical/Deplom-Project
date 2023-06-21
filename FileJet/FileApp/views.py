#эта функция используется для извлечения объекта из базы данных с использованием модели и ее первичного ключа
from django.shortcuts import render, redirect, get_object_or_404
#эта функция используется для извлечения объекта из базы данных с использованием модели и ее первичного ключа
from django.contrib.auth.decorators import login_required
# оператор импорта 
from .models import File, Category, Chat, Message
# оператор импорта 
from .forms import FileForm

from django.contrib.auth.models import User

from ProfileApp.models import Profile

from django.http import JsonResponse

# Create your views he
#декоратор, що використовується в Django для вказівки того, що функція подання або подання на основі класів потребують аутентифікації
@login_required(login_url='main')
#file_pk представляет собой заполнитель для первичного ключа (или любого другого уникального идентификатора) файла. 
def show_file(request, file_pk):
    #як порожній словник, ви можете пізніше заповнити його парами ключ-значення
    context={}
    #функція швидкого доступу
    file = get_object_or_404(File, pk=file_pk)
    #file додає отриманий Fileоб'єкт (file) у contextсловник з ключем "file". Це дозволяє передати Fileоб'єкт як змінну шаблон для рендерингу або подальшої обробки.
    context["file"] = file
    
    context["is_uploader"] = False  

    if file.user == request.user:
        context["is_uploader"] = True
        chats = Chat.objects.filter(file = file)
        # context["chats"] = chats
        chat_and_last_message_list = []
        for chat in chats:
            chat_and_last_message = []
            try:
                last_message = Message.objects.filter(chat = chat).order_by('pk').latest('pk')
            except Message.DoesNotExist:
                last_message = ''
            profile_image = Profile.objects.get(user = chat.send_user)

            chat_and_last_message.append(profile_image)

            chat_and_last_message.append(last_message)

            chat_and_last_message.append(chat)

            chat_and_last_message_list.append(chat_and_last_message)
        context["chat_and_last_message_list"] = chat_and_last_message_list
    
    #return render(request, 'file.html', context)' використовується для рендерингу шаблону з ім'ям 'file.html' з наданими даними context і повернення HTTP-відповіді. У Django функція `render()` використовується для рендерингу шаблону з даними контексту та створення HTTP-відповіді, який буде повернутий клієнту
    return render(request, 'file.html', context)





#декоратор, що використовується в Django для вказівки того, що функція подання або подання на основі класів потребують аутентифікації
@login_required(login_url='main')
#file_pk представляет собой заполнитель для первичного ключа (или любого другого уникального идентификатора) файла. 
def show_upload_file(request):
    #обробки відправлення форм або будь-яких інших дій, які змінюють дані на сервері
    if request.method == "POST":
        #використовується для створення екземпляра класу форми
        form = FileForm(request.POST, request.FILES)
        #використовується для перевірки правильності надісланих даних форми
        if form.is_valid():
            #используется для сохранения данных формы в качестве нового экземпляра модели без немедленной фиксации их в базе данных.
            form_saved = form.save(commit=False)
            #призначає поточного користувача
            form_saved.user = request.user
            category = Category.objects.get_or_create(name = request.POST.get("category"))
            #надає значення поля "категорія", отримане зі словника
            form_saved.category = category[0]


            file_size = request.POST.get("file-size-bytes")
            profile = Profile.objects.get(user = request.user)


            profile.used_size += int(file_size)

            profile.save()

            #используется для сохранения измененных данных формы, 
            form_saved.save()
            #використовується для перенаправлення користувача на певну URL
            return redirect('main')
        #використовується для друку помилок перевірки, що виникли під час перевірки форми.
        print(form.errors)
        #використовується для перенаправлення користувача на певну URL-адресу
        return redirect('upload_file')
    else:
         #як порожній словник, ви можете пізніше заповнити його парами ключ-значення
        context = {}
        #извлекает все объекты из Categoryмодели.
        categories = Category.objects.all()
        #categories додає categoriesнабір запитів у contextсловник, роблячи його доступним для шаблону під час рендерингу.
        context["categories"] = categories
        #створює екземпляр класу FileForm форми
        form = FileForm()
        #form додає categoriesнабір запитів у contextсловник, роблячи його доступним для шаблону під час рендерингу.
        context["form"] = form
        #даними та повертає оброблений шаблон у вигляді HTTP-відповіді
        return render(request, 'upload_file.html', context)
    
#декоратор, що використовується в Django для вказівки того, що функція подання або подання на основі класів потребують аутентифікації
@login_required(login_url='main')
#
def error404(request, exception=None):
    return render(request, 'error404.html', status=404)


@login_required(login_url='main')
def create_chat(request):
    if request.method == "GET":
        file_owner_pk = request.GET.get("fileOwnerPk")
        file_pk = request.GET.get("filePk")
        chat_pk = request.GET.get("ChatExPk")
        if chat_pk == '':
            current_user = request.user
            file_user = User.objects.get(pk = file_owner_pk)
            file = File.objects.get(pk = file_pk)

            try:
                chat_index = Chat.objects.latest('pk').pk
            except:
                chat_index = 1

            chat_name = f"""Chat №{chat_index}"""
            chat = Chat.objects.get_or_create(send_user = current_user, file = file, receive_user = file_user)
            if chat[1]:
                chat = chat[0]
                chat.name = chat_name
                chat.save()
            else:
                chat = chat[0]
                chat_name = chat.name
        else:
            chat = Chat.objects.get(pk = chat_pk)
            chat_name = chat.name
        return JsonResponse({"chat_pk":chat.pk, "chat_name": chat_name})


@login_required(login_url='main')
def create_message(request):
    if request.method == "GET":
        message_content = request.GET.get("messageContent")
        chat_pk = request.GET.get("chatPk")

        chat = Chat.objects.get(pk = chat_pk)


        is_uploader = False
        if chat.receive_user == request.user:
            is_uploader = True

        message = Message.objects.create(chat = chat, user = request.user, message = message_content)
        message.save()
        message_user = Profile.objects.get(user = request.user)
        message_user_image = message_user.image.url

        return JsonResponse({"chat_name":chat.name, "user_image":message_user_image, "message":message_content, "is_uploader": is_uploader})


@login_required(login_url='main')
def get_messages(request):
    if request.method == "GET":
        chat_pk = request.GET.get("chatPk")
        chat = Chat.objects.get(pk = chat_pk)
        messages = Message.objects.filter(chat = chat).values()
        messages = list(messages)

        send_user = request.user

        send_profile = Profile.objects.get(user = chat.send_user)

        send_profile_pk = send_profile.user.pk

        send_profile_image_path = send_profile.image.url

        

        receive_profile = Profile.objects.get(user = chat.receive_user)

        receive_profile_pk = receive_profile.user.pk

        receive_profile_image_path = receive_profile.image.url

        # first sender, second receiver
        users = [send_profile_image_path, receive_profile_image_path]

        users_pks = [send_profile_pk, receive_profile_pk]
        print(users_pks, users)
        return JsonResponse({"messages":messages, "users": users, "users_pks": users_pks})