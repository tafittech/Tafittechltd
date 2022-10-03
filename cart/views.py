from django.shortcuts import render, redirect



#imports from apps here.
from .models import Carts




# Create your views here.
def cart_home_page(request):
    cart_id = request.session.get('cart_id', None)
    qs = Carts.objects.filter(id=cart_id)
    if cart_id is None:
        if qs.count() == 1:
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Carts.objects.new_cart(user=request.user)
            request.session['cart_id']=cart_obj.id
    return render(request, 'cart/cart-home.html', {})








def update_cart(request):
    return render(request,'cart/update-cart.html',{})