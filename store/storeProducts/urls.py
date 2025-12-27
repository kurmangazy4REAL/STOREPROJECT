from django.contrib import admin
from django.urls import path
from storeProducts.views import index, products, basket_add, basket_remove
app_name = 'products'
urlpatterns = [
    path('', index, name='main'),
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('products/', products, name='products'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]   