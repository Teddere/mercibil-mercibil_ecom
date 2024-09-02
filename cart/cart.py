from decimal import Decimal
from django.conf import settings
from articles.models import Article


class Cart():

    def __init__(self,request):
        self.session= request.session

        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        # Accessibilité du panier
        self.cart = cart

    def add(self,article,quantity=1):
        art_id = str(article.id)
        if art_id not in self.cart:
            self.cart[art_id] = {
                'quantity':quantity,
                'price': str(article.price)
            }
        else:
            self.cart[art_id]['quantity'] += quantity
        print(self.cart)
        self.session.modified = True

    def remove(self,article):
        art_id = str(article.id)
        if art_id in self.cart:
            del self.cart[art_id]
        self.session.modified = True

    def get_total(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        for key in list(self.cart.keys()):
            del self.cart[key]
        self.session.modified = True

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        art_ids = self.cart.keys()
        articles = Article.objects.filter(id__in=art_ids)
        cart = self.cart.copy()
        for art in articles:
            cart[str(art.id)]['article'] = art
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item



