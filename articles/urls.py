from django.urls import path
from articles.views import (ArticleListView,ArticleCreateView,ArticleUpdateView,CategoryListView,category_delete)


app_name = 'articles'


urlpatterns = [
    path('',ArticleListView.as_view(),name='list'),
    #path('<str:slug>/',ArticleListView.as_view(),name='category_detail'),
    path('new/',ArticleCreateView.as_view(),name='new'),
    path('<str:slug>/edit/',ArticleUpdateView.as_view(),name='edit'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/delete/',category_delete,name='category_delete'),
]

