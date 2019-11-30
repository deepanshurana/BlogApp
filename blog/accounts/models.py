from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='users')

    #ADDITIONAL FIELDS

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    profilePic = models.ImageField(default='default.jpg', upload_to='profilepics/')
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    bio = models.CharField(max_length=256)

    def __str__(self):
        return '{}'.format(self.user.username,)

