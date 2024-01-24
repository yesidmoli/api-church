
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    cellular = models.CharField(max_length=15)
    type_document = models.CharField(max_length=50)
    document = models.CharField(max_length=20 ,unique=True)


    def __str__(self):
        return f'Client: {self.name} '
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
    
