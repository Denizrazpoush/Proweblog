from django.shortcuts import render
from .models import Article


# Create your views here.

def detail_view(request, pk):

    articles = Article.article_manager.all()

    return render(request, "blog_app/post-details.html", {"articles": articles})






