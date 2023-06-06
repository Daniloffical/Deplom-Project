from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='registration')
def show_profile(request):
    context = {}
    profile = Profile.objects.get(user=request.user)
    context['profile'] = profile
    return render(request, 'profile.html', context)