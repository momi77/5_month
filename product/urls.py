from django.urls import path
from .views import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoriesListAPIView,
    CategoryDetailAPIView,
    ReviewsListAPIView,
    ReviewsDetailAPIView,
)

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:id>/', ProductDetailAPIView.as_view()),
    path('categories/', CategoriesListAPIView.as_view()),
    path('categories/<int:id>/', CategoryDetailAPIView.as_view()),
    path('reviews/', ReviewsListAPIView.as_view()),
    path('reviews/<int:id>/', ReviewsDetailAPIView.as_view()),
]
