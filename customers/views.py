from django.http import JsonResponse
from django.views.generic import ListView
from django.core.paginator import PageNotAnInteger, EmptyPage
from customers.models import Customer
# Email function send
from shopping.utils import send_email
# form customer
from customers.forms import CustomerForm
from customers.utils import generate_password
from datetime import datetime


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
        context = { }

        customer_id = request.POST.get('id') if request.POST.get('id') else None

        if customer_id != 'undefined' and customer_id is not None:
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                context['status'] = 'danger'
                context['message'] = 'Cette action ne peut être exécuter !'
                return JsonResponse(context, status=400)
        else:
            customer = None

        form = CustomerForm(request.POST,instance=customer,user=customer.user)
        if form.is_valid():
            form.save()
            # Send email
            template_email = 'customers/customer_mail.html'
            receivers = ['localhost']
            context_mail = {
                'username': request.POST.get('username'),
                'email': request.POST.get('email'),
                'phone': request.POST.get('phone'),
            }
            send_email('Modification de données client',receivers,template_email,context_mail)
            context['status'] = 'success'
            context['message'] = 'Les informations du clients ont été modifier avec succès !'
        return JsonResponse(context)












