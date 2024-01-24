from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount_available = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()


    def __str__(self):
        return f'Product: {self.name}'
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"