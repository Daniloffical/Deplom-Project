from django.shortcuts import render
# Create your views here.
def show_about_us(request):
    return render (request, 'about_us.html')


