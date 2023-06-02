from django.shortcuts import render

# Create your views here.
def show_enter(request):
    return render(request, 'enter.html')