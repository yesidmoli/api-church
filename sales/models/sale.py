from django.db import models
from .client import Client
from .product import Product

"""Model to register sales """
class Sale(models.Model):
    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True),
    value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pagada', 'Pagada'),('A Crédito', 'A Crédito')])


    def __str__(self):
        return f'{self.client}, {self.product}'
    
    
    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"
