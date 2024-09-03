from django.contrib.gis.geometry import json_regex
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from articles.models import Article
from cart.cart import Cart

# cart page view content
class CartView(TemplateView):
    template_name = 'cart/cart_main.html'

    def get_context_data(self, **kwargs):
        cart = Cart(self.request)
        context = super().get_context_data(**kwargs)
        context['cart_articles'] = cart
        context['cart_total'] = cart.get_total()
        return context



def cart_add(request):
    context = {}
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        article_id = int(request.POST.get('article_id'))
        article_qty = int(request.POST.get('article_qty',1))
        article_override = bool(request.POST.get('article_override',False))
        art = get_object_or_404(Article, id=article_id)

        cart.add(article=art, quantity=article_qty, override=article_override)
        cart_quantity = len(cart)
        context['quantity'] = cart_quantity
        context['message'] = f"L'article {art.name} a bien été rajouter dans le panier"

        return JsonResponse(context)
    context['message'] = 'Non valid'
    return JsonResponse(context)
def cart_update(request):
    context = {}
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        article_id = int(request.POST.get('article_id'))
        article_qty = int(request.POST.get('article_qty', 1))
        art = get_object_or_404(Article, id=article_id)
        cart.update(article=art, quantity=article_qty)
        context['message'] = f"L'article {art.name} a bien été rajouter dans le panier"
        return JsonResponse(context)
    context['message'] = 'Non valid'
    return JsonResponse(context)



def cart_delete(request):
    context = {}
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        article_id = int(request.POST.get('article_id'))
        art = get_object_or_404(Article, id=article_id)
        cart.remove(article=art)
        context['message'] = f"L'article {art.name} a bien été retirer dans le panier"
        return JsonResponse(context)
    context['message'] = 'Non valid'
    return JsonResponse(context)


