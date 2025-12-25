from rest_framework import serializers
from product.models import ProductModel, CategoryModel, ReviewModel

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = 'id title price category'.split()

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'