from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from products.models import Category, Product

def homepage(request):
    return HttpResponse("Welcome to Dewi's Blooms!")

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def search(request):
    """A view to handle product search queries."""
    query = request.GET.get('q', None)
    products = Product.objects.all()
    categories = Category.objects.all()

    if query:
        # Filter products by name or description containing the query term
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    context = {
        'products': products,
        'categories': categories,
        'search_term': query,
    }
    return render(request, 'home/search_results.html', context)

def products_view(request):
    categories = Category.objects.all()  # Get all categories
    products_by_category = {
        category: Product.objects.filter(category=category)  # Group products by category
        for category in categories
    }
    return render(request, 'products.html', {'products_by_category': products_by_category, 'categories': categories})