from django.db import models
from users.models import Users

# Create your models here.
class storeCategories(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True,null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class storeProducts(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
    image = models.TextField()
    category = models.ForeignKey(
    storeCategories,
    on_delete=models.CASCADE,
    null=True,    
    blank=True   
)
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
  
    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
    

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)
    
class Basket(models.Model):
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    product = models.ForeignKey(to=storeProducts, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'
    
    def sum(self):
        return self.product.price * self.quantity