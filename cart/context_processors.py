from cart.cart import Cart
# Rendre accessible le panier sur toutes les pages

def cart(request):
    return {'cart': Cart(request)}