from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("title/<str:title_>", views.title, name="title"),
    path("create_new_page", views.newpage, name="newpage"),
    path("title/<str:title>/editpage", views.editpage, name="editpage"),
    path("title/<str:title>/editpage/edit", views.edit, name="edit"),
    path("random", views.randompage, name="random"),
]
