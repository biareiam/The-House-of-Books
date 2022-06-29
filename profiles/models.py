"""Models for profiles app """
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

from events.models import Event


class UserProfile(models.Model):
    """
    User Profile model, extending User model with onetoone relationship.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
        )
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
        )
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(
        blank_label='Choose country from dropdown',
        null=True,
        blank=True)

    def __str__(self):
        """string method, return user name"""
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create instance of UserProfile each time instance of User is created.
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


class SavedEventList(models.Model):
    """
    To hold the event(s) that a user can save to their profile.
    """
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    event = models.ManyToManyField(Event, blank=True)

    def __str__(self):
        """string method, return 'username's saved events'"""
        return f'{self.user.user.username}\'s saved events'
