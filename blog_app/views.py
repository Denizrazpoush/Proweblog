from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Comment , Message
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import Contactus
from .forms import MessageForm



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


def search(request):

    q = request.GET.get("q")
    articles = Article.article_manager.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)
    return render(request, "blog_app/blog.html", {"articles": objects_list})


def contact(request):



    if request.method == "POST":
        form = MessageForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            Message.objects.create(title=title, text=text, email=email)


            return redirect("home_app:home")
        else:
            form = MessageForm(data=request.POST)

    else:
        form = MessageForm()

    return render(request, "blog_app/contact.html", {"form": form})






