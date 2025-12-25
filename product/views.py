from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import ProductModel, CategoryModel, ReviewModel
from product.serializers import CategoryListSerializer, ProductListSerializer, ReviewListSerializer

@api_view(['GET'])
def products_list_api_view(request):
    products = ProductModel.objects.all()
    data = ProductListSerializer(products, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def products_detail_api_view(request, product_id):
    try:

        product = ProductModel.objects.get(id=product_id)
        data = ProductListSerializer(product, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    
    except ProductModel.DoesNotExist:

        return Response(data={
            'error': 'product does not exist'
        }, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def categories_list_api_view(request):
    categories = CategoryModel.objects.all()
    data = CategoryListSerializer(categories, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def categories_detail_api_view(request, category_id):
    try:
        category = CategoryModel.objects.get(id=category_id)
        data = CategoryListSerializer(category, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    except CategoryModel.DoesNotExist:
        return Response(data={
            'error': 'category does mot exist'
        }, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def reviews_list_api_view(request):
    reviews = ReviewModel.objects.all()
    data = ReviewListSerializer(reviews, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def reviews_detail_api_view(request, review_id):
    try:
        review = ReviewModel.objects.get(id=review_id)
        data = ReviewListSerializer(review, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    except ReviewModel.DoesNotExist:
        return Response(data={
            'error': 'review does mot exist'
        }, status=status.HTTP_404_NOT_FOUND)
