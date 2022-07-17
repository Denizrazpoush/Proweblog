from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def detail_view(request, slug):

    article = get_object_or_404(Article, slug=slug)
    if request.method == "POST":
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        parent = Comment.objects.get(id=parent_id)
        Comment.objects.create(body=body, user=request.user, article=article, parent=parent)

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




