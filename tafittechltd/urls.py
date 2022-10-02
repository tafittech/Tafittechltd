from django.conf import settings
from django.conf.urls.static import static



from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('', include('products.urls')),
    path('', include('search.urls')),
]


if settings.DEBUG:
    urlpatterns =  urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns =  urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)