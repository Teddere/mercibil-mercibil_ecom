from django.core.paginator import PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from articles.models import Article,Category,ArticleImage
from articles.forms import CategoryForm


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_main.html'
    context_object_name = 'articles'
    paginate_by = 5
    ordering = ['-created']

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

# Category list view content
class CategoryListView(ListView):
    model = Category
    template_name = 'articles/category_main.html'
    paginate_by = 4
    ordering = ['name']

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

    def post(self, request, *args, **kwargs):
        context = { }

        category_id = request.POST.get('id') if request.POST.get('id') else None

        if category_id != 'undefined' and category_id:
            try:
                category = Category.objects.get(id=category_id)

            except Category.DoesNotExist:
                context['status'] = 'danger'
                context['message'] = 'Cette action ne peut être exécuter !'
                return JsonResponse(context,status=400)


        else:
            category = None
        form = CategoryForm(request.POST, request.FILES,instance=category)

        if form.is_valid():
            form.save()
            msg = 'Nouvelle catégorie ajoutée avec succès !' if category_id =='undefined' else 'La catégorie a bien été modifier avec succès !'
            messages.success(request, msg)
            context['status'] = 'success'
            return JsonResponse(context,status=200)
        else:
            context['errors'] = form.errors.as_json()
            context['status'] = 'warning'
            context['message'] = 'Les informations entrées ne sont pas acceptables !'

        return JsonResponse(context,status=400)

# category delete view content
def category_delete(request):
    context= {}
    if request.method == 'POST':
        category_id = request.POST.get('id')
        try:
            category = Category.objects.get(id=category_id)
            category.delete()
            messages.success(request,'La suppression a bien été exécuté !')
            context['status'] = True
        except Category.DoesNotExist:
            messages.error(request,"Cette catégorie n'existe pas !")
        except:
            messages.error(request,'La suppression a échouée !')
    context['status'] = False

    return JsonResponse(context)
