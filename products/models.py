from email.policy import default
from pyexpat import model
from ssl import create_default_context
from trace import Trace
from xml.etree.ElementTree import QName
from django.urls import reverse
from random  import Random
import os
from django.db.models import Q
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
class ProductQuerySet(models.query.QuerySet):
    

    def featured(self):
        return self.filter(featured=True)

    def search(self, query):
        lookups = (
            Q(title__icontains=query)| 
            Q(description__icontains=query)| 
            Q(price__icontains=query)
            )
        return self.filter(lookups).distinct()



class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)


    def all(self):
        return self.get_queryset().all()
    
    def featured(self):
        return self.get_queryset().featured()

    def get_by_pk(self, pk):
        qs = self.get_queryset().filter(pk=pk)
        if qs.count() == 1:
            return qs.first()
        return None
    
    def search(self, query):
        return self.get_queryset().search(query)



# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=19, default=0.00)
    image       = models.ImageField(upload_to='products/', null=True, blank=True)
    featured    = models.BooleanField(default=False)
    tags        = models.ManyToManyField('Tag', blank=True)
    vote_total  = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio  = models.IntegerField(default=0, null=True, blank=True)
    create      = models.DateField(auto_now_add=True)


    objects = ProductManager()


    def get_absolute_url(self):
        return reverse("detail", kwargs={ "slug":self.slug})

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down','Down Vote')
    )
    #owner =
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=500)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

