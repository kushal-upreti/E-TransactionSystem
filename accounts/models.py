from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    name=models.CharField(max_length=200)
    email= models.EmailField(unique=True)
    phone_no=models.CharField(max_length=20, unique=True)
    avatar=models.ImageField(default="avatar.svg", null=True, blank=True, upload_to="images")
    address=models.CharField(null=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name