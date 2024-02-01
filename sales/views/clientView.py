"""Import the viewsets for ModelViewSet"""
from rest_framework import viewsets



from rest_framework.response import Response
from django.db.models import Sum

from rest_framework import generics,authentication,permissions

from rest_framework.generics import ListAPIView
#serializers
from sales.serializers.clientSerializer import ClientSerializer,ClientListSerializer


#models
from sales.models.client import Client



class ClientViewset(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request, *args, **kwargs):

        # Obtener el conjunto de consultas en tiempo real
        queryset = self.get_queryset()

        # Obtener la cantidad total de clientes
        total_clients = queryset.count()

        # Serializar y devolver la respuesta
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'total_clients': total_clients,
            'clients': serializer.data,
        }

        return Response(data)
    

class ClientListView(ListAPIView):
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]




