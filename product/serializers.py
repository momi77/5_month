from rest_framework import serializers
from .models import ProductModel, ReviewModel, CategoryModel
from django.db.models import Avg

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ['id', 'text', 'star']

class ProductListSerializer(serializers.ModelSerializer):
    reviews = ReviewListSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = ['id', 'title', 'description', 'price', 'reviews', 'average_rating']

    def get_average_rating(self, obj):
        avg = obj.reviews.aggregate(avg_stars=Avg('star'))['avg_stars']
        return avg or 0

class CategoryListSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'products_count']


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'name']


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['id', 'title', 'description', 'price', 'category']


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ['id', 'text', 'star', 'product']
