from django.urls import include, path


from .views import product_page, product_detail, featured_detail, featured_product


urlpatterns =[
    path('products/', product_page, name='list'),
    path('products/<str:slug>', product_detail, name='detail'),
    path('featured/', featured_product,name='featured'),
    path('featured/<str:slug>',featured_detail,name='f_detail'),

]