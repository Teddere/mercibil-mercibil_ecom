from django.core.paginator import PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from django.shortcuts import render
from articles.models import Article,Category,ArticleImage


# Category list view content
class CategoryListView(ListView):
    model = Category
    template_name = 'articles/category_main.html'
    context_object_name = 'categories'
    paginate_by = 5

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

# category delete view content
def category_delete(request):
    pass