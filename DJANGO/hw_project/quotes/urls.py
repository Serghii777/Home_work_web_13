from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('author/<str:author_id>/', views.author_detail),
    path('tag/<int:tag_id>/', views.quotes_by_tag, name='quotes_by_tag'),
    path('top-ten-tags/', views.top_ten_tags, name='top_ten_tags'),
]