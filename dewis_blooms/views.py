from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse("Welcome to Dewi's Blooms!")


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def search(request):
    # Placeholder logic for search functionality delete later

    return render(request, 'home/search_results.html')