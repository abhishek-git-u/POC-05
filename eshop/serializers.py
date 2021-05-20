from rest_framework import serializers
from eshop.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','description','category','brand','size','date_added' ,'product_image']
