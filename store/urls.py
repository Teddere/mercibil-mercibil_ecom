from django.urls import path
from store.views import (HomeView, CatalogView, ArticleDetailView, CartView, RegisterView,LoginView)

app_name = 'store'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalog/',CatalogView.as_view(), name='catalog'),
    path('catalog/<slug:slug>/',CatalogView.as_view(), name='catalog_detail'),
    path('articles/<slug:slug>/',ArticleDetailView.as_view(), name='article_detail'),
    path('cart/',CartView.as_view(), name='cart'),
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(), name='login'),
]