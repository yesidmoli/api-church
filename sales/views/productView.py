from rest_framework import viewsets

#serializers
from sales.serializers.productSerializer import ProductSerializer

from django.http import HttpResponseNotFound

#models
from sales.models.product import Product


class ProductViewset(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
   