from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from FileApp.models import File, Category
from .forms import FileForm


# Create your views he


def show_file(request, file_pk):
    file = get_object_or_404(File, pk=file_pk)
    print(file)
    return render(request, 'file.html')

def show_upload_file(request):
    if request.method == "POST":
        # file_image = request.POST.get("img")
        # file_name = request.POST.get("name")
        # file_description = request.POST.get("description")
        # file_category_pk = request.POST.get("category")
        # file_private = request.POST.get("private")
        # file_category = Category.objects.get(pk = file_category_pk)
        # if file_private == "on":
        #     file_private = True
        # elif file_private == None:
        #     file_private = False
        # file = File.objects.create(name = file_name, description = file_description, category=file_category, private = file_private, image=file_image, user=request.user)
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            form_saved = form.save(commit=False)
            form_saved.user = request.user
            form_saved.save()
            return redirect('main')
        return redirect('upload_file')
    else:
        context = {}
        categories = Category.objects.all()
        context["categories"] = categories
        form = FileForm()
        context["form"] = form
        return render(request, 'upload_file.html', context)