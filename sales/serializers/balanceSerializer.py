from rest_framework import serializers

#models
from sales.models.balance import Balance
from sales.models.product import Product
from sales.models.sale import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:

        model = Sale
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model= Product
        fields = '__all__'

class BalanceSerializer(serializers.ModelSerializer):

    producto = ProductSerializer()
    sale = SaleSerializer()

    class Meta:
        model = Balance
        fields = '__all__'