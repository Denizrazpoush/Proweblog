from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

# Create your models here.


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(status=True)


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
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    upload = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(default=now)
    objects = models.Manager()
    article_manager = ArticleManager()

#     it can be changes to Newest update Time

    def __str__(self):
        return self.title

