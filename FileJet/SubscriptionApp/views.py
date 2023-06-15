from django.shortcuts import render
from .models import Subscription


# Create your views here.
def show_subscription(request):
    context = {}
    subscriptions = Subscription.objects.all()
    for subscription in subscriptions:
        subscription.description = list(subscription.description.split("`"))
    context["subscriptions"] = subscriptions
    return render(request, "subscription.html", context)