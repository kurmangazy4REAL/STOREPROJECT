from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from storeProducts.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='index'),
    path('products/',include('storeProducts.urls', namespace='product')),
    path('users/',include('users.urls', namespace='users')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)