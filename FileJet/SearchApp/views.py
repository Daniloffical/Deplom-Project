from django.shortcuts import render
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='main')
def show_search(request):
    return render(request, 'search.html')