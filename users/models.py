from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission



class User(AbstractUser):
    full_name = models.CharField(max_length=50, null=True)
    artistic_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True,error_messages={"unique":"This field must be unique."})

    groups = models.ManyToManyField(Group, related_name="custom_user_set")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_set")
