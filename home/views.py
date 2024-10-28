from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def search(request):
    # Basic placeholder logic for the search functionality delete later
    return render(request, 'home/search_results.html')


def shopping_bag(request):
    return render(request, 'home/shopping_bag.html')


def index(request):
    # Calculate grand_total based on cart items (this is just a placeholder)
    grand_total = 0  # Replace with actual calculation if needed

    # Pass the value to the template
    return render(request, 'home/index.html', {'grand_total': grand_total})
