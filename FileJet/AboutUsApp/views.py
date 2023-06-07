from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='main')
def show_about_us(request):
    return render (request, 'about_us.html')


