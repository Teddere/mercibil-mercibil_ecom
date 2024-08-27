from django.urls import path
from articles.views import (CategoryListView)


app_name = 'articles'


urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category'),
]

