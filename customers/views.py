from django.views.generic import ListView
from django.contrib import messages
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.http import JsonResponse,QueryDict
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