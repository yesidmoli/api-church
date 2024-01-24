from rest_framework import viewsets

from django.http import HttpResponseNotFound

#serializers
from sales.serializers.balanceSerializer import BalanceSerializer

#model
from sales.models.balance import Balance

#filter


class BalanceViewset(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
   