from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.

def detail_view(request, slug):

    article = get_object_or_404(Article, slug=slug)

    return render(request, "blog_app/post-details.html", {"article": article})


def blog_view(request):

    articles = Article.objects.all()
    return render(request, "blog_app/blog.html", {"articles": articles})








