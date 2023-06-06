from django import template
from ProfileApp.models import Profile


register = template.Library()


@register.simple_tag
def give_user(request):
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user)
        return profile