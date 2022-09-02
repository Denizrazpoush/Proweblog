from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
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
    category = models.ManyToManyField(Category, related_name="articles")
    title = models.CharField(max_length=30)
    body = models.TextField()
    status = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    upload = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(default=now)
    objects = models.Manager()
    article_manager = ArticleManager()
    slug = models.SlugField(max_length=100, unique=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog_app:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return self.title


class Comment (models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ('-created_at',)

    def __str__(self):
        return self.body[:50]


class Message(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.title








