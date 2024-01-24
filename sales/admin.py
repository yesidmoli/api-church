#django
from django.contrib import admin

"""from sales.models.sale import Sale
from sales.models.product import Product
from sales.models.client import Client
from sales.models.balance import Balance
from sales.models.payment import Payment
from sales.models.debt import Debt"""

from sales.models import *

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    """Sale admin."""

    list_display = (
        'id',
        'client',
        'product',
        'amount',
        'date',  
        'status',
    )

    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin."""

    list_display = (
        'id',
        'name',
        'amount_available',
        'unit_price',
    )

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Client admin."""

    list_display = (
        'id',
        'name',
        'cellular',
        'document',
    )


admin.site.register(Balance)
admin.site.register(Payment)
admin.site.register(Debt)
