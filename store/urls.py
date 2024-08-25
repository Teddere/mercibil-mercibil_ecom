from django.urls import path
from store.views import (HomeView,CatalogView,ArticleDetailView)

app_name = 'store'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalog/',CatalogView.as_view(), name='catalog'),
    path('catalog/<slug:slug>/',CatalogView.as_view(), name='catalog_detail'),
    path('articles/<slug:slug>/',ArticleDetailView.as_view(), name='article_detail'),
]