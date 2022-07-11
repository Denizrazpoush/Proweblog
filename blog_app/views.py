from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def detail_view(request, slug):

    article = get_object_or_404(Article, slug=slug)

    return render(request, "blog_app/post-details.html", {"article": article})


def blog_view(request):

    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)

    return render(request, "blog_app/blog.html", {"articles": objects_list})


def category_detail(request, pk):

    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()

    return render(request, "blog_app/blog.html", {"articles": articles})




