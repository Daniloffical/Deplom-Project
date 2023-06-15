from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from FileApp.models import File, Category
from .forms import FileForm


# Create your views he

@login_required(login_url='main')
def show_file(request, file_pk):
    context={}
    file = get_object_or_404(File, pk=file_pk)
    context["file"] = file
    return render(request, 'file.html', context)

@login_required(login_url='main')
def show_upload_file(request):
    if request.method == "POST":
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
    
@login_required(login_url='main')
def error404(request, exception=None):
    return render(request, 'error404.html', status=404)