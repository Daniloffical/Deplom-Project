from django import template
from ProfileApp.models import Profile
from django.contrib.auth.decorators import login_required

register = template.Library()

@login_required(login_url='/example url you want redirect/')
@register.simple_tag
def give_user(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        return profile