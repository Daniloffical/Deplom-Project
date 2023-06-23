from django.shortcuts import render, redirect

from ProfileApp.models import Profile

from FileApp.models import File
 # Create your views here.
def show_main(request):
    if request.method == "POST":

        searched = request.POST.get("search-content")

        return redirect("search", searched)
    return render(request, 'main.html')
