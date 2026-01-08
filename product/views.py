from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import ProductModel, CategoryModel, ReviewModel
from django.db.models import Count
from product.serializers import (
    CategoryListSerializer,
    ProductListSerializer,
    ReviewListSerializer,
    CategoryCreateSerializer,
    ProductCreateSerializer,
    ReviewCreateSerializer
)


@api_view(['GET', 'POST'])
def products_list_api_view(request):
    if request.method == 'GET':
        products = ProductModel.objects.prefetch_related('reviews').all()
        data = ProductListSerializer(products, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def products_detail_api_view(request, product_id):
    try:
        product = ProductModel.objects.get(id=product_id)
    except ProductModel.DoesNotExist:
        return Response(
            {'error': 'product does not exist'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        data = ProductListSerializer(product).data
        return Response(data)

    elif request.method == 'PUT':
        serializer = ProductCreateSerializer(
            product,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
@api_view(['GET', 'POST'])
def categories_list_api_view(request):
    if request.method == 'GET':
        categories = CategoryModel.objects.annotate(
            products_count=Count('productmodel_set')
        )
        data = CategoryListSerializer(categories, many=True).data
        return Response(data=data)


    elif request.method == 'POST':
        serializer = CategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def categories_detail_api_view(request, category_id):
    try:
        category = CategoryModel.objects.get(id=category_id)
    except CategoryModel.DoesNotExist:
        return Response(
            {'error': 'category does not exist'},
            status=404
        )

    if request.method == 'GET':
        data = CategoryListSerializer(category).data
        return Response(data)

    elif request.method == 'PUT':
        serializer = CategoryCreateSerializer(
            category,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=204)

    
@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = ReviewModel.objects.all()
        data = ReviewListSerializer(reviews, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        serializer = ReviewCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, review_id):
    try:
        review = ReviewModel.objects.get(id=review_id)
    except ReviewModel.DoesNotExist:
        return Response(
            {'error': 'review does not exist'},
            status=404
        )

    if request.method == 'GET':
        data = ReviewListSerializer(review).data
        return Response(data)

    elif request.method == 'PUT':
        serializer = ReviewCreateSerializer(
            review,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=204)

