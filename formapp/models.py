from django.db import models


# Create your models here.
class UserProfileInfo(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True)
