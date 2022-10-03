from django.urls import path




#import your views here.
from .views import cart_home_page, update_cart





#add your urls path here.

urlpatterns = [
    path('cart/', cart_home_page, name='cart'),
    path('update/', update_cart, name='update'),
]
