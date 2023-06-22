from django.shortcuts import render
from django.contrib.auth.decorators import login_required 

from FileApp.models import File

# Create your views here.
@login_required(login_url='main')
def show_search(request):
    files = File.objects.filter(name__unaccent__icontains = 1)
    # name__unaccent__icontains
    return render(request, 'search.html')