from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Exclude the rating field
        exclude = ('rating',)
        fields = '__all__'  # This includes all fields from the Product model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Customize the category field to use friendly names
        categories = Category.objects.all()
        friendly_names = [(category.id, category.get_friendly_name()) for category in categories]
        self.fields['category'].choices = friendly_names

        # Add custom CSS classes to fields for consistent styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'