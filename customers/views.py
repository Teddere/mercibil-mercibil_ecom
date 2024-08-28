from django.shortcuts import render
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from customers.models import Customer

class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'customers/customer_main.html'
    paginate_by = 6

    def paginate_queryset(self, queryset, page_size):
        paginator = self.get_paginator(queryset, page_size)
        page = self.request.GET.get('page')

        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        return (paginator,page_obj,page_obj.object_list,page_obj.has_other_pages())


