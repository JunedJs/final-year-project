from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.profiles.models import *

# Create your models here.
class organization(models.Model):
    companyName = models.CharField(max_length = 300)
    profile = models.OneToOneField(commonProfile,on_delete = models.CASCADE)
    industry = models.CharField(max_length = 200)
    companySize=models.CharField(max_length = 100)
    specialties = models.CharField(max_length = 300)

    def __str__(self):
        return self.companyName



# end date changes to be done with experience form to be completed by tommorow