from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from FileApp.models import File, Category


# Create your views he


def show_file(request):
    return render(request, 'file.html')

def show_upload_file(request):
    if request.method == "POST":
        file_image = request.POST.get("img")
        file_name = request.POST.get("name")
        file_description = request.POST.get("description")
        file_category_pk = request.POST.get("category")
        file_private = request.POST.get("private")
        file_category = Category.objects.get(pk = file_category_pk)
        if file_private == "on":
            file_private = True
        elif file_private == None:
            file_private = False
        file = File.objects.create(name = file_name, description = file_description, category=file_category, private = file_private, image=file_image, user=request.user)
        return redirect('main')
    context = {}
    categories = Category.objects.all()
    context["categories"] = categories
    return render(request, 'upload_file.html', context)