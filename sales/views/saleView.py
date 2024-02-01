"""Import the viewsets for ModelViewSet"""
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView


#auth
from rest_framework import generics,authentication,permissions

from django.http import HttpResponseNotFound
from rest_framework import status

from django.db.models import Sum

#Serializers
from sales.serializers.saleSerializer import SaleSerializer, SaleListSerializer, AbonoSerializer, ClientDetailSerializer


#models
from sales.models.sale import Sale

#filter
from sales.filters import SaleFilter


#view Sale
class SaleViewSet(viewsets.ModelViewSet):

    serializer_class = SaleSerializer
    queryset = Sale.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):

        #obtenemos los datos de la solicitud
        data = request.data

        #verificamos si el cliente tiene alguna deuda pendiente
        client_id = data.get('client')
        
        if Sale.objects.filter(client_id = client_id, status = 'A Crédito').exists():
            return Response({'error':'El cliente tiene deudas pendientes. No se puede realizar otra venta a crédito.'}, status=status.HTTP_400_BAD_REQUEST)

        # Si no hay deudas pendientes, procede con la creación normal
        return super().create(request, *args, **kwargs)

    
class SaleListView(ListAPIView):
    serializer_class = SaleListSerializer
    queryset = Sale.objects.all().order_by('-id')
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = SaleFilter
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    


    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        # Obtener todas las ventas pagadas y en crédito
        paid_sales = queryset.filter(status='Pagada')
        credit_sales = queryset.filter(status='A Crédito')

        # Calcular el total de las ventas pagadas y las que deben 
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

class AbonoView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        abono_serializer = AbonoSerializer(data=request.data)
        
        if abono_serializer.is_valid():
            abono_serializer.create(abono_serializer.validated_data)
            return Response("Abono registrado exitosamente.")
        else:
            return Response(abono_serializer.errors, status=400)
        

class ClientDetailView(RetrieveAPIView):
    serializer_class = ClientDetailSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        client_id = kwargs.get('pk')
        sales = Sale.objects.filter(client_id=client_id)

        if sales.exists():
            # Obtener el total de abonos del cliente y la cantidad de abonos
            total_abonos_cliente = sum(sale.value for sale in sales.filter(is_abono=True))
            cantidad_abonos = sales.filter(is_abono=True).count()

            # Serializar y devolver respuesta
            serializer = self.get_serializer(sales, many=True)

            data = {
                'total_abonos_cliente': total_abonos_cliente,
                'cantidad_abonos': cantidad_abonos,
                'sales': serializer.data
            }

            return Response(data)
        else:
            return Response({'error': 'Cliente no encontrado'}, status=404)
