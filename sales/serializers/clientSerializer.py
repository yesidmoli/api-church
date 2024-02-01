from rest_framework import serializers

from sales.models.client import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class ClientListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id' , 'name']


