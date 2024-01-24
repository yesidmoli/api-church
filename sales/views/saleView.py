"""Import the viewsets for ModelViewSet"""
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from django.http import HttpResponseNotFound

from django.db.models import Sum

#Serializers
from sales.serializers.saleSerializer import SaleSerializer, SaleListSerializer


#models
from sales.models.sale import Sale

#filter
from sales.filters import SaleFilter


#view Sale
class SaleViewSet(viewsets.ModelViewSet):

    serializer_class = SaleSerializer
    queryset = Sale.objects.all()

   

    
class SaleListView(ListAPIView):
    serializer_class = SaleListSerializer
    queryset = Sale.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = SaleFilter


    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        # Obtener todas las ventas pagadas y en crédito
        paid_sales = queryset.filter(status='Pagada')
        credit_sales = queryset.filter(status='A Crédito')

        # Calcular el total de las ventas pagadas y las que deben en Python
        total_paid_sales = sum(sale.value for sale in paid_sales) if paid_sales.exists() else 0
        total_credit_sales = sum(sale.value for sale in credit_sales) if credit_sales.exists() else 0

        """
        # Agregar los totales al contexto del serializador
        context = {
            'total_paid_sales': total_paid_sales,
            'total_credit_sales': total_credit_sales,
        }

        # Llamar a la función list del Mixin de la vista
        serializer = self.get_serializer(queryset, many=True, context=context)"""

        #serializar y devolver respuesta
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'total_paid_sales': total_paid_sales,
            'total_credit_sales': total_credit_sales,
            'sales': serializer.data
        }

        return Response(data)
        