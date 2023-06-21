from django.shortcuts import render
from .models import Subscription
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='main')
def show_subscription(request):
    context = {}
    subscriptions = Subscription.objects.all()
    for subscription in subscriptions:
        subscription.description = list(subscription.description.split("`"))
    context["subscriptions"] = subscriptions
    return render(request, "subscription.html", context)