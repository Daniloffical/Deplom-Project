from django.shortcuts import render

# Create your views he
def show_file(request):
    return render(request, 'file.html')

def show_upload_file(request):
    return render(request, 'upload_file.html')