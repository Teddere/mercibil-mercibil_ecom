from django.core.paginator import PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import ListView, UpdateView,CreateView
from django.shortcuts import render, redirect
from articles.models import Article,Category,ArticleImage
from articles.forms import CategoryForm,ArticleForm


# Article list view content
class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_main.html'
    context_object_name = 'articles'
    paginate_by = 5
    ordering = ['created']

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
# Article create view content
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle'] = 'Créer un nouvel article'
        return context

    def post(self, request, *args, **kwargs):
        context = {
            'pageTitle': 'Créer un nouvel article'
        }
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            if request.FILES.get('images'):
                for image in request.FILES.getlist('images'):
                    ArticleImage.objects.create(article=article,image=image)

            messages.success(request, f"L'article {article.name} a été ajouté avec succès !")
            return redirect('articles:list')
        else:
            messages.warning(request, "La création d'un nouvel article a échoué ..!")
        context['form'] = form
        return render(request,'articles/article_detail.html',context)

# Article update view content
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pageTitle']= 'Modification de l\'article'
        context['images'] = ArticleImage.objects.filter(article=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        context = {
            'pageTitle': 'Modification de l\'article'
        }
        article = self.get_object()
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()

            if request.FILES.get('images'):
                for image in request.FILES.getlist('images'):
                    ArticleImage.objects.update_or_create(article=article,image=image)
            messages.success(request,"La mise de l'article "+article.name+" a été mis à jour ...!")
            return redirect('articles:list')
        else:
            context['form'] = form
            context['images'] = ArticleImage.objects.filter(article=article)
        messages.error(request,'La modification a échouée. Veuillez réessayer !')
        return render(request,'articles/article_detail.html',context)




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
