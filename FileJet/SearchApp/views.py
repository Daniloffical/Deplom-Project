from django.shortcuts import render
from django.contrib.auth.decorators import login_required 

from FileApp.models import File

# Create your views here.
@login_required(login_url='main')
def show_search(request, searched):
    if request.method == "POST":
        searched = request.POST.get("searched")
    context = {}
    files = File.objects.filter(name__icontains = searched)
    context["files"] = files
    return render(request, 'search.html', context)