from django.db import models

from .client import Client

class Debt(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount_to_collected = models.DecimalField(max_digits=10, decimal_places=2)
    clients_who_owe= models.IntegerField()

    def __str__(self):
        return f'Debt: {self.client}'
    
    class Meta:
        verbose_name = "Debt"
        verbose_name_plural = "Debts"