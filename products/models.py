from random  import Random
import os
import re
from django.db import models
from django.db.models.signals import pre_save, post_save


from .utils import unique_slug_generator




def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def  upload_image_path(instance, filename):
    new_filename   =Random.randint(1,9999)
    name, ext      =get_filename_ext(filename)
    final_filename = f'new_filename'.format(new_filename=new_filename, ext=ext)
    return 'product/'f'new_filename/'f'final_filename'.format(
        new_filename=new_filename,
        final_filename=final_filename
        )
# Create Your Model Manager here.


class ProductManager(models.Manager):
    def featured(self):
        return self.get_queryset().filter(featured=True)




# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=19, default=0.00)
    image       = models.ImageField(upload_to='products/', null=True, blank=True)
    featured    = models.BooleanField(default=False)

    objects = ProductManager()


    def get_absolute_url(self):
        return "/products_detail/{slug}".format(slug=self.slug)

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
