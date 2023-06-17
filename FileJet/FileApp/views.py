#эта функция используется для извлечения объекта из базы данных с использованием модели и ее первичного ключа
from django.shortcuts import render, redirect, get_object_or_404
#эта функция используется для извлечения объекта из базы данных с использованием модели и ее первичного ключа
from django.contrib.auth.decorators import login_required
# оператор импорта 
from FileApp.models import File, Category
# оператор импорта 
from .forms import FileForm


# Create your views he
#декоратор, що використовується в Django для вказівки того, що функція подання або подання на основі класів потребують аутентифікації
@login_required(login_url='main')
#file_pk представляет собой заполнитель для первичного ключа (или любого другого уникального идентификатора) файла. 
def show_file(request, file_pk):
    #як порожній словник, ви можете пізніше заповнити його парами ключ-значення
    context={}
    #функція швидкого доступу
    file = get_object_or_404(File, pk=file_pk)
    #fileдодає отриманий Fileоб'єкт (file) у contextсловник з ключем "file". Це дозволяє передати Fileоб'єкт як змінну шаблон для рендерингу або подальшої обробки.
    context["file"] = file
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