from django.shortcuts import redirect, render
from django.views.generic import ListView,CreateView
from django.contrib import messages
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from users.models import Shopper
# Email function send
from shopping.utils import send_email
# form customer
from customers.models import Customer
from customers.forms import  CustomerCreateForm, CustomerUpdateForm
from customers.utils import generate_password

class CustomerListView(ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'customers/customer_main.html'
    paginate_by = 6
    ordering = '-created'

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
        context = {}

        customer_id = request.POST.get('id', None)
        post_data = request.POST.copy()
        post_data['username'] = post_data['username'].replace(' ', '_').title()
        # update customer data
        if customer_id and customer_id != 'undefined':
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                context['status'] = 'danger'
                context['message'] = "Ce client n'existe pas sur la plateforme !"
                return JsonResponse(context,status=400)

            form = CustomerUpdateForm(post_data, instance=customer,user=customer.user)
            if form.is_valid():
                form.save()
                # Sending emails
                template_email = "customers/customer_email.html"
                subject = "Modification de données client"
                receivers = ['localhost']
                context_email = {
                    'username': post_data['username'].replace('_', ' ').title(),
                    'email': post_data['email'],
                    'phone': post_data['phone'],
                }
                send_email(subject,receivers,template_email, context_email)
                context['status'] = 'success'
                messages.success(request, f'Les informations du client {post_data['username']} ont été mis à jour')
                return JsonResponse(context,status=200)
        # Create customer data
        else:
            post_data['password'] = generate_password()
            form = CustomerCreateForm(post_data)
            if form.is_valid():
                shopper = form.save()
                if form.cleaned_data['phone']:
                    shopper.customer.phone = form.cleaned_data['phone']
                    shopper.customer.save()
                # Sending emails
                template_email = "customers/customer_email.html"
                subject = "Nouveau client"
                receivers = ['localhost']
                context_email = {
                        'username': post_data['username'].replace('_', ' ').title(),
                        'email': post_data['email'],
                        'phone': post_data['phone'],
                        'password': post_data['password'],
                    }
                send_email(subject, receivers, template_email, context_email)
                context['status'] = 'success'
                messages.success(request,f'Le client {shopper.username} a bien été rajouter dans la liste des clients')
                return JsonResponse(context)
            else:
                context['status'] = 'warning'
                context['message'] = 'Les formations entrées ne sont pas acceptables !'
                return JsonResponse(context,status=400)

class CustomerCreateView(CreateView):
    model = Shopper
    form_class = CustomerCreateForm
    template_name = 'customers/customer_new.html'

    def post(self, request, *args, **kwargs):
        context = {}
        post_data = request.POST.copy()
        post_data['username'] = post_data['username'].replace(' ', '_').title()
        post_data['password'] = generate_password()
        form = CustomerCreateForm(post_data)
        if form.is_valid():
            shopper = form.save()
            if form.cleaned_data['phone']:
                shopper.customer.phone = form.cleaned_data['phone']
                shopper.customer.save()
            # Sending emails
            template_email = "customers/customer_email.html"
            subject = "Nouveau client"
            receivers = ['localhost']
            context_email = {
                'username': post_data['username'].replace('_', ' ').title(),
                'email': post_data['email'],
                'phone': post_data['phone'],
                'password': post_data['password']
            }
            send_email(subject, receivers, template_email, context_email)
            context['status'] = 'success'
            messages.success(request, f'Le client {shopper.username} a bien été rajouter dans la liste des clients')
            return redirect('customer:list')
        else:
            errors_messages = []
            for field,errors in form.errors.items():
                for error in errors:
                    errors_messages.append(f'{field}: {error}')
            error_msg = ' '.join(errors_messages)
            messages.warning(request, f"Le client n'a pas pu être créer ! Erreurs : {error_msg}")

            context['status'] = 'warning'

            return render(request, self.template_name, context)




def customer_delete(request):
    context = {}
    if request.method == 'POST' and request.POST.get('id'):
        customer_id = request.POST.get('id')
        try:
            customer = Customer.objects.get(id=customer_id)
            name = customer.user.username.replace('_',' ')
            customer.delete()
            messages.success(request,f"Le client {name} a bien été supprimer sur la plateforme !")
            context['status'] = True
        except Customer.DoesNotExist:
            context['status'] = False
            messages.error(request,"Le client n'existe pas sur la plateforme !")
            return JsonResponse(context,status=400)
        return JsonResponse(context)

