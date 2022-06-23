from django.shortcuts import render
from blog_app.models import Article, ArticleManager

# Create your views here.


def home(request):

    articles = Article.objects.all()
    print(Article.article_manager.all())

    return render(request, 'home_app/index.html', {'articles': articles})
