from rest_framework import serializers
from models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    amount = serializers.IntegerField()

    def create(self, validated_data):
        return Product(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        return instance
