from django import template

register = template.Library()

@register.simple_tag
def calculate_bag_total(bag):
    return sum(item['price'] * item['quantity'] for item in bag.values())