from django.views.generic import TemplateView, ListView, DetailView, CreateView,FormView
from django.shortcuts import redirect,render
from django.core.paginator import EmptyPage,PageNotAnInteger
from django.contrib import messages
from users.forms import RegisterShopperUser,LoginFormUser
from users.models import Shopper
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
# article detail page view content
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'store/main_article.html'
    object = 'article'

# cart page view content
class CartView(TemplateView):
    template_name = 'store/main_cart.html'
# Register shopper view content
class RegisterView(CreateView):
    model = Shopper
    form_class = RegisterShopperUser
    template_name = 'store/main_register.html'

    def post(self, request, *args, **kwargs):
        context = { }
        form = RegisterShopperUser(request.POST)

        if form.is_valid():
            user = form.save()
            messages.success(request, f'Compte de {user.username} créé avec succès !')
            return redirect('store:home')
        messages.error(request, 'Le compte n\'a pas pu être créer !')
        context["form"] = form
        return render(request, self.template_name, context)
# Login page view content
class LoginView(FormView):
    form_class = LoginFormUser
    template_name = 'store/main_login.html'

class DashboardView(TemplateView):
    pass




