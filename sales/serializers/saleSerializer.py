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


class SaleSerializerDetail(serializers.ModelSerializer):
    client = ClientSerializer()  # Agregar el serializador del cliente para incluir información del cliente

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
        ordering = ['-date']

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


class AbonoSerializer(serializers.Serializer):
    sale_id = serializers.IntegerField()
    value = serializers.IntegerField()
    concept = serializers.CharField(max_length=255, required=False )

    def create(self, validated_data):
        id = validated_data['sale_id']
        value= validated_data['value']
        concept = validated_data['concept']

        venta_original = Sale.objects.get(id=id)

        # Resta el valor del abono al valor de la venta
        venta_original.value -= value

        # Actualiza el estado de la venta según el valor
        if venta_original.value <= 0:
            venta_original.status = 'Cerrada'
            venta_original.value = 0
        else:
            venta_original.status = 'A Crédito'

        # Guarda los cambios en la venta
        venta_original.save()

        # Crea un nuevo registro en la tabla Venta con el monto del abono y el Concepto
        Sale.objects.create(
            client=venta_original.client,
            product=venta_original.product,
            amount=venta_original.amount,
            date=venta_original.date,
            value=value,
            status='Pagada',
            concept=concept,
            is_abono=True
        )

class ClientDetailSerializer(serializers.ModelSerializer):
    
    client = ClientSerializer()
    product = ProductSerializer()

    # total_value = serializers.SerializerMethodField()

    class Meta:

        model = Sale
        fields = '__all__'

