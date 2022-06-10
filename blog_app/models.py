from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

# Create your models here.


class Category(models.Model):

    title = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, unique_for_date="pub_date")
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    upload = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(default=now)
#     it can be changes to Newest update Time

    def __str__(self):
        return self.title
