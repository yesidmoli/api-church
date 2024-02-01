from django.db import models
from .client import Client
from .product import Product


"""Model to register sales """
class Sale(models.Model):
    client= models.ForeignKey(Client, on_delete=models.CASCADE )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(error_messages={'required': 'El  campo cantidad no puede estar vacío'})
    date = models.DateField(auto_now_add=True)
    value = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('Pagada', 'Pagada'),('A Crédito', 'A Crédito'), ('Cerrada', 'Cerrada')], error_messages={'invalid': 'Introduzca un número válido con hasta dos decimales.',
                                                                                                                                                'blank': '¡Ups! Este campo es obligatorio.',
                                                                                                                                                
            'null': '¡Ups! Este campo no puede ser nulo.',})
    is_abono = models.BooleanField(default=False)
    concept = models.CharField(max_length=255, blank=True, null=True)




    def save(self, *args, **kwargs):
        if self.status == 'A Crédito' and self.is_abono:
            # Resta el valor del abono al valor de la venta
            # self.value -= self.value

            # Actualiza el estado de la venta según el valor restante
            if self.value <= 0:
                self.status = 'Cerrada'
                self.value = 0
            else:
                self.status = 'A Crédito'

        super(Sale, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.client}, {self.product}'
    
    
    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"
