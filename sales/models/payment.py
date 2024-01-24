from django.db import models

from .sale import Sale

class Payment(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True),
    value = models.DecimalField(max_digits=10, decimal_places=2)
    concept = models.CharField(max_length=255)

    def __str__(self):
        return f'Payment: {self.sale}'
    
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"