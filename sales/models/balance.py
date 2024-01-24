from django.db import models

from .sale import Sale
from .client import Client
from .product import Product

class Balance(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'Balance: {self.sale} '
    
    class Meta:
        verbose_name = "Balance"
        verbose_name_plural = "Balances"