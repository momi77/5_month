from rest_framework import serializers
from .models import ProductModel, ReviewModel, CategoryModel
from django.db.models import Avg
from common.validators import validate_user_age_for_product, moderator_cannot_create

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

    def validate(self, attrs):

        moderator_cannot_create(self.context['request'].user)

        validate_user_age_for_product(self.context['request'].user)

        return attrs


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
    name = serializers.CharField(
        max_length=255,
        required=True,  
        allow_blank=False 
    )

    class Meta:
        model = CategoryModel
        fields = ['id', 'name']

    def validate_name(self, value):
        if CategoryModel.objects.filter(name=value).exists():
            raise serializers.ValidationError("Категория с таким именем уже существует")
        return value


class ProductCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, required=True, allow_blank=False)
    description = serializers.CharField(max_length=1000, required=True)
    price = serializers.FloatField(min_value=0)  # цена >= 0
    category = serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all())

    class Meta:
        model = ProductModel
        fields = ['id', 'title', 'description', 'price', 'category']


    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Название товара должно быть минимум 3 символа")
        return value


class ReviewCreateSerializer(serializers.ModelSerializer):
    text = serializers.CharField(required=True, allow_blank=False)
    star = serializers.IntegerField(min_value=1, max_value=5) 
    product = serializers.PrimaryKeyRelatedField(queryset=ProductModel.objects.all())

    class Meta:
        model = ReviewModel
        fields = ['id', 'text', 'star', 'product']

