from rest_framework import serializers

from sales.models.sale import Sale

#serializer externos
from sales.serializers.productSerializer import ProductSerializer
from sales.serializers.clientSerializer import ClientSerializer

#serializer POST, PUT DELETE
class SaleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sale
        fields = '__all__'

#serializer for list sales whith products, and client
class SaleListSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer()
    product = ProductSerializer()

    # total_value = serializers.SerializerMethodField()

    class Meta:

        model = Sale
        fields = '__all__'

    def get_total_value(self, obj):
        return obj.total_value
    
     # Incluye los totales en el serializador
    """def to_representation(self, instance):
        data = super().to_representation(instance)

        
        Add the context
        data['total_paid_sales'] = self.context['total_paid_sales']
        data['total_credit_sales'] = self.context['total_credit_sales']


        # Agregar el total_value al resultado serializado
        data['total_value'] = instance.total_value

        return data"""

