from django.shortcuts import render
from django.db.models import Q
from products.models import Product, Category


def index(request):
    """ A view to return the index page """
    # Placeholder for calculating grand_total if needed
    grand_total = 0  # Modify as required for cart total calculations
    return render(request, 'home/index.html', {'grand_total': grand_total})


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


def shopping_cart(request):
    """A view to display the shopping bag"""
    return render(request, 'home/shopping_cart.html')