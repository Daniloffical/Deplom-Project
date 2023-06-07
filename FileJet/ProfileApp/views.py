from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='main')
def show_profile(request):
    context = {}
    profile = Profile.objects.get(user=request.user)
    context['profile'] = profile
    return render(request, 'profile.html', context)

@login_required(login_url='main')
def log_out(request):
    logout(request)
    return redirect("main")