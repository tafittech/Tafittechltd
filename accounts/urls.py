from django.urls import path    


from .views import home_page ,account , accounts, login_page, register_page

urlpatterns =[
path('response/', home_page),
path('',accounts),
path('login/',login_page),
path('register/', register_page),
path('accounts/<str:pk>', account),
]