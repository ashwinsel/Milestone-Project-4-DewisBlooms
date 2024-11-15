from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Represents a product in the store, linked to a category,
    with details like price, rating, and images.
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        """
        Validate the product's rating to ensure it's between 0 and 5.
        """
        if self.rating is not None and (self.rating < 0 or self.rating > 5):
            raise ValidationError("Rating must be between 0 and 5.")