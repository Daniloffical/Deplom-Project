from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views he


def show_file(request):
    return render(request, 'file.html')

def show_upload_file(request):
    return render(request, 'upload_file.html')