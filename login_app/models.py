from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Profile(models.Model):

    title = models.CharField(max_length=20)
    mothers_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
