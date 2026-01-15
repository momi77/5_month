
from django.contrib import admin
from django.urls import path, include
from product.views import (
    CategoryDetailAPIView,
    CategoriesListAPIView, 
    ProductListAPIView,
    ProductDetailAPIView,
    ReviewsListAPIView,
    ReviewsDetailAPIView,
    )

producturlpatterns = [
    # path('api/v1/products/', products_list_api_view),
    path('api/v1/products/', ProductListAPIView.as_view()),
    path('api/v1/products/<int:id>/', ProductDetailAPIView.as_view()),
    path('api/v1/categories/', CategoriesListAPIView.as_view()),
    path('api/v1/categories/<int:id>/', CategoryDetailAPIView.as_view()),  
    path('api/v1/reviews/', ReviewsListAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', ReviewsDetailAPIView.as_view()),
]


urlpatterns = producturlpatterns + [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    
]


