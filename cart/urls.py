from django.urls import path
from cart.views import (CartView,cart_add,cart_update)

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='list'),
    path('add/', cart_add, name='create'),
    path('update/', cart_update, name='update'),
    path('delete/', cart_update, name='delete'),
]