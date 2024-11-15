from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    """A user profile model for storing default delivery info and order history"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, blank=True, null=True)
    default_postcode = models.CharField(max_length=20, blank=True, null=True)
    default_town_or_city = models.CharField(max_length=40, blank=True, null=True)
    default_street_address1 = models.CharField(max_length=80, blank=True, null=True)
    default_street_address2 = models.CharField(max_length=80, blank=True, null=True)
    default_county = models.CharField(max_length=80, blank=True, null=True)
    # Additional fields for special dates and preferences
    anniversary_date = models.DateField(blank=True, null=True)
    birthday_date = models.DateField(blank=True, null=True)
    favorite_flowers = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = [
            'default_phone_number', 'default_postcode', 'default_town_or_city', 
            'default_street_address1', 'default_street_address2', 'default_county', 
            'anniversary_date', 'birthday_date', 'favorite_flowers'
        ]

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Create or update the user profile"""
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # Only update if profile already exists, avoiding potential errors on first save
        instance.userprofile.save()
