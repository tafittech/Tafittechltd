from django.shortcuts import render, redirect

# Create your views here.
def cart_home_page(request):
    return render(request, 'cart/cart-home.html', {})








def update_cart(request):
    return render(request,'cart/update-cart.html',{})