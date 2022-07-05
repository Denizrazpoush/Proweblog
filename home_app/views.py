from django.shortcuts import render
from blog_app.models import Article, ArticleManager, Category

# Create your views here.


def home(request):

    articles = Article.objects.all()
    recent = Article.objects.all()

    return render(request, 'home_app/index.html', {'articles': articles, 'recent': recent})
