from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from django.contrib import messages

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
        
    # Get user’s order history if Order model exists
    orders = Order.objects.filter(user_profile=user_profile)

    context = {
        'form': form,
        'orders': orders
    }
    return render(request, 'profiles/profile.html', context)

def order_history(request, order_number):
    """Display past order details from the user's profile"""
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, f'You are viewing a past order confirmation for order number {order_number}.')

    context = {
        'order': order,
        'from_profile': True,  # Add this to distinguish from regular checkout success
    }

    return render(request, 'checkout/checkout_success.html', context)