from django.urls import path
from . import views

app_name = "blog_app"
urlpatterns = [

    path("detail/<slug:slug>", views.detail_view, name="detail"),
    path("blogs/", views.blog_view, name="blogs"),
    path("category/<int:pk>", views.category_detail, name="category"),

]
