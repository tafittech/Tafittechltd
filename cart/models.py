from django.conf import settings
from django.db import models


#imports from app modules.

from products.models import Product

#create model manager here 
class CartModelManger(models.Manager):
    def new_cart(self, user=None):
        user_obj =None
        if user is not None:
            if user.is_authenticated():
                user_obj = user_obj
        return self.model.objects.create(user=user_obj)


User = settings.AUTH_USER_MODEL
# Create your models here.
class Carts(models.Model):
    user       = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    products   = models.ManyToManyField(Product, blank=True)
    subtotal   = models.DecimalField(default=0.00, decimal_places=2, max_digits=9999)
    total      = models.DecimalField(default=0.00, decimal_places=2, max_digits=9999)
    update     = models.TimeField(auto_now=True)
    timestamp  = models.TimeField(auto_now_add=True)


    objects = CartModelManger()




    def __str__(self):
        return str(self.id)