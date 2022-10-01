from django.urls import path    


from .views import home_page ,account , accounts, login_page, register_page

urlpatterns =[
#path('response/', home_page),
path('',accounts, name='home'),
path('login/',login_page, name='login'),
path('register/', register_page, name='register'),
path('accounts/<str:pk>', account, name='account'),
]