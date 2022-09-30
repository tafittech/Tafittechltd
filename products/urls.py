from django.urls import include, path


from .views import product_page, product_detail, featured_detail, featured_product


urlpatterns =[
    path('products/', product_page),
    path('products_detail/<str:slug>', product_detail),
    path('featured/', featured_product),
    path('featured_detail/<str:slug>',featured_detail),

]