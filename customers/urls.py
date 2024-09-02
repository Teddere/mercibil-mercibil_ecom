from django.urls import path
from customers.views import (CustomerListView,CustomerCreateView,customer_delete)

app_name = 'customers'
urlpatterns = [
    path('',CustomerListView.as_view(), name='list' ),
    path('new/',CustomerCreateView.as_view(), name='create'),
    path('delete/',customer_delete,name='delete' ),
]