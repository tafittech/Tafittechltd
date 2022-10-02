from cgitb import lookup
from turtle import title
from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product

# Create your views here.

class SearchPage(ListView):
    template_name ='search/search.html'

    def qet_context_data(self, *arg, **kwargs):
        context = super(SearchPage,self).get_context_data(*arg,**kwargs)
        context['query']=self.request.GET.get('Q')
        return context
    
    def get_queryset(self):
        request = self.request
        query   = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
        
        
        