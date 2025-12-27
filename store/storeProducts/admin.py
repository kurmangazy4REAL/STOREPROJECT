from django.contrib import admin
from storeProducts.models import storeProducts, storeCategories,Basket

# Register your models here.

admin.site.register(storeCategories)



@admin.register(storeProducts)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', 'price', 'quantity', 'image', 'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',) 


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    readonly_fields = ('created_timestamp',)
    extra = 0