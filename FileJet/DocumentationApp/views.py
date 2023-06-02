from django.shortcuts import render

# Create your views here.
def show_documentation(request):
    return render(request, 'documentation.html')

def show_documentation_accounts(request):
    return render(request, 'documentation_accounts.html')

def show_documentation_confident(request):
    return render(request, 'documentation_confident.html')

def show_documentation_files(request):
    return render(request, 'documentation_files.html')