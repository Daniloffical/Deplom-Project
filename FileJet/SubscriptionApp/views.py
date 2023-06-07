from django.shortcuts import render

# Create your views here.
def show_subscription(request):
    return render(request, "subscription.html")