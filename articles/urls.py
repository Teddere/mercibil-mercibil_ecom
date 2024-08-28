from django.urls import path
from articles.views import (CategoryListView,category_delete)


app_name = 'articles'


urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/delete/',category_delete,name='category_delete'),
]

