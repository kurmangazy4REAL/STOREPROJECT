from django.contrib import admin

from users.models import Users
from storeProducts.admin import BasketAdmin


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = [BasketAdmin,]