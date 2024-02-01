from rest_framework import viewsets
from rest_framework import generics,authentication,permissions
#serializers
from sales.serializers.productSerializer import ProductSerializer

from django.http import HttpResponseNotFound

#models
from sales.models.product import Product


class ProductViewset(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
   