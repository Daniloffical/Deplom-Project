from django.shortcuts import render

from ProfileApp.models import Profile
 # Create your views here.
def show_main(request):
    return render(request, 'main.html')
