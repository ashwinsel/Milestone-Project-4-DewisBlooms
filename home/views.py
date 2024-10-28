from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')


def search(request):
    # Basic placeholder logic for the search functionality delete later
    return render(request, 'home/search_results.html')


def shopping_bag(request):
    return render(request, 'home/shopping_bag.html')