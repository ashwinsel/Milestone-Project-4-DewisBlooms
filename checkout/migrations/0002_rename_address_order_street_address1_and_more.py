# Generated by Django 5.1.2 on 2024-11-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='street_address1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='town_or_city',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
        migrations.AddField(
            model_name='order',
            name='street_address2',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
