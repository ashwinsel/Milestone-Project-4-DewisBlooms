from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = (
        'order_number', 
        'date', 
        'delivery_cost', 
        'order_total', 
        'grand_total'
    )
    fields = (
        'order_number',
        'date', 
        'full_name', 
        'email', 
        'phone_number', 
        'address', 
        'city',
        'postcode', 
        'county', 
        'country', 
        'delivery_cost', 
        'order_total', 
        'grand_total'
    )
    list_display = (
        'order_number',
        'user_profile',
        'full_name',
        'email',
        'phone_number',
        'date',
        'order_total',
        'grand_total',
        'original_bag',
        'stripe_pid',
    )
    
    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)