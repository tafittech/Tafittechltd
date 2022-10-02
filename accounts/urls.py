from django.urls import path    


from .views import home_page ,account , accounts, login_page, register_page,contact_form

urlpatterns =[
#path('response/', home_page),
path('',accounts, name='home'),
path('login/',login_page, name='login'),
path('register/', register_page, name='register'),
path('contact/', contact_form, name='contact'),
]