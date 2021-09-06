from django.db import models
from django import forms
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    game_flag = models.BooleanField(default=False)
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional attributes you want
    club_location = models.CharField(max_length=40, blank=True)
    rating = models.IntegerField(default=0, blank=False, null=False)
    antal_vunna = models.IntegerField(default=0, blank=False, null=False)
    ratingf = models.FloatField(default=100, blank=False, null=False)
    snitt = models.FloatField(default=0, blank=False, null=False)
    match_uppdate = models.CharField(max_length=100, blank=True)
    matcher = models.CharField(max_length=2000, blank=True)
    ratings = models.DecimalField(max_digits=9, decimal_places=2, default=1000, blank=False, null=False)
    
    def __str__(self):
        return self.user.username