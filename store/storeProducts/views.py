from django.shortcuts import render, HttpResponseRedirect
from storeProducts.models import storeProducts, storeCategories
from storeProducts.models import Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request):
    context = {'title': 'Kurmangazy-Store'}
    return render(request, 'storeProducts/index.html',context)

def products(request,category_id=None, page_number=1):
    products = storeProducts.objects.filter(category_id = category_id) if category_id else storeProducts.objects.all()

    per_page = 3
    paginator = Paginator(products, 3)
    products_paginator = paginator.page(page_number)


    context = {
        'title': 'Products Catalog',
        'categories': storeCategories.objects.all(),
        'products': products_paginator,
     }
    return render(request, 'storeProducts/products.html',context)

@login_required
def basket_add(request, product_id):
    product = storeProducts.objects.get(id=product_id)
    basket_var = Basket.objects.filter(user=request.user, product=product)

    if not basket_var.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = basket_var.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, basket_id):
    basket= Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))