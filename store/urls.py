from django.urls import path
from store.views import (HomeView,CatalogView,ArticleDetailView,CartView)

app_name = 'store'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalog/',CatalogView.as_view(), name='catalog'),
    path('catalog/<slug:slug>/',CatalogView.as_view(), name='catalog_detail'),
    path('articles/<slug:slug>/',ArticleDetailView.as_view(), name='article_detail'),
    path('cart/',CartView.as_view(), name='cart'),
]