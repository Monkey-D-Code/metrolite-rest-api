from rest_framework import serializers
from . models import Item_sale, Item_purchase

class Item_saleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item_sale
        fields = '__all__'

class Item_purchaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item_purchase
        fields = '__all__'