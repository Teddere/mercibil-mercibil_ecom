from django.urls import path
from customers.views import (CustomerListView,customer_delete)

app_name = 'customers'
urlpatterns = [
    path('',CustomerListView.as_view(), name='list' ),
    path('delete/',customer_delete,name='delete' ),
]