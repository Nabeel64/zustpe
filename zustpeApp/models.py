from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    userpic = models.ImageField(upload_to="profliepics/",default="user.png")
