from django.views.generic import TemplateView,ListView
from django.shortcuts import redirect
from django.core.paginator import EmptyPage,PageNotAnInteger
from articles.models import Article, Category


# Home page view content
class HomeView(TemplateView):
    template_name = 'store/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all().order_by('-created')[:4]
        context['categories'] = Category.objects.all()
        return context


# catalog page view content

class CatalogView(ListView):
    model = Article
    template_name = "store/main_catalog.html"
    paginate_by = 12

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            try:
                category = Category.objects.get(slug=slug)
            except Category.DoesNotExist:
                return redirect('store:catalog')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = self.kwargs.get('slug')
        return context

    def get_queryset(self):
        slug = self.kwargs.get('slug')

        if slug:
            return super().get_queryset().filter(category__slug=slug)[::-1]
        return super().get_queryset()[::-1]


    def pagination(self,queryset,page_size):

        paginator = self.get_paginator(queryset, page_size)
        page = self.request.GET.get('page')
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        return (paginator,page_obj,page_obj.object_list,page_obj.has_other_pages())
