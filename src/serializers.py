from rest_framework import serializers
from .models import Product, Order, Customer, Tag

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name', 'price', 'category', 'description', 'date_created', 'tags')