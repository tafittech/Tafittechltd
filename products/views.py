from django.shortcuts import render

from .models import Product

# Create your views here.

def product_page(request):
    queryset = Product.objects.all()
    context ={
        'object_list':queryset
    }
    return render(request,'products/products.html',context)


def featured_product(request):
    instance = Product.objects.featured()
    context ={
        'featured_list':instance
    }
    return render(request,'products/featured.html',context)




def product_detail(request, slug):
    instance = Product.objects.get(slug=slug)
    context ={
        'object':instance
    }
    return render(request,'products/products_detail.html',context)


def featured_detail(request, slug):
    instance = Product.objects.featured()
    slug      = Product.objects.get(slug=slug)
    context ={
        'object':slug
    }
    return render(request,'products/featured_detail.html',context)