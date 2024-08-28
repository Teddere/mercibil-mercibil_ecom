from django.urls import path
from articles.views import (ArticleListView,CategoryListView,category_delete)


app_name = 'articles'


urlpatterns = [
    path('',ArticleListView.as_view(),name='list'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/delete/',category_delete,name='category_delete'),
]

