from django.shortcuts import render, redirect
from .models import Subscription
from django.contrib.auth.decorators import login_required
from ProfileApp.models import Profile

# Create your views here.
@login_required(login_url='main')
def show_subscription(request):
    context = {}
    subscriptions = Subscription.objects.all()
    for subscription in subscriptions:
        subscription.description = list(subscription.description.split("`"))

    profile = Profile.objects.get(user = request.user)
    context["profile"] = profile


    context["subscriptions"] = subscriptions
    return render(request, "subscription.html", context)

def disable_subscription(request):
    profile = Profile.objects.get(user = request.user)

    subscription = Subscription.objects.get(pk = 1)

    profile.subscription = subscription

    profile.save()

    return redirect('subscription')

def enable_subscription(request, subscription_pk):
    profile = Profile.objects.get(user = request.user)

    subscription = Subscription.objects.get(pk = subscription_pk)

    profile.subscription = subscription

    profile.save()

    return redirect('profile')