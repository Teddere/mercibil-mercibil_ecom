from django.views.generic import TemplateView, ListView, DetailView, CreateView,FormView
from django.shortcuts import redirect,render
from django.core.paginator import EmptyPage,PageNotAnInteger
from django.contrib import messages
from users.forms import RegisterShopperUser,LoginFormUser
from users.models import Shopper
from articles.models import Article, Category
from shopping.utils import send_email
from django.contrib.auth import authenticate, login, logout



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

# Register shopper view content
class RegisterView(CreateView):
    model = Shopper
    form_class = RegisterShopperUser
    template_name = 'store/main_register.html'

    def post(self, request, *args, **kwargs):
        context = { }
        post_data = request.POST.copy()
        if not post_data['password1'] or post_data['password1'] != post_data['password']:
            form = RegisterShopperUser(post_data)
            messages.warning(request, 'Le mot de passe est incorrect.')
            context['form'] = form
            return render(request, self.template_name, context)


        post_data['username'] = post_data['username'].replace(' ', '_').title()
        form = RegisterShopperUser(post_data)

        if form.is_valid():
            shopper = form.save()
            messages.success(request, f"Compte de {shopper.username} a été  créé avec succès !")

            """ Sending Email
            subject = "Bienvenue sur mercibil"
            receivers = ["localhost"]
            template_email = "customers/customer_email.html"
            context_email = {
                'username': post_data['username'].replace('_', ' ').title(),
                'email': post_data['email'],
            }
            send_email(subject, receivers, template_email, context_email)
             end email"""
            return redirect('store:login')
        messages.error(request, 'Le compte n\'a pas pu être créer !')
        context["form"] = form
        return render(request, self.template_name, context)
# Login page view content
class LoginView(FormView):
    form_class = LoginFormUser
    template_name = 'store/main_login.html'
    def post(self, request, *args, **kwargs):
        context = { }
        form = LoginFormUser(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('store:dashboard')
        messages.warning(request,'Votre email ou mot de passe est incorrect !')
        context["form"] = form

        return render(request, self.template_name, context)



class DashboardView(TemplateView):
    template_name = 'store/main_dashboard.html'




