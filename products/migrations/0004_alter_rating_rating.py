# Generated by Django 5.1.2 on 2024-11-16 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_rating_product_average_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
