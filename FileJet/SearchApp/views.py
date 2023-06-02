from django.shortcuts import render

# Create your views here.
def show_search(request):
    return render(request, 'search.html')