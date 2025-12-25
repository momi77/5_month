
from django.contrib import admin
from django.urls import path
from product.views import (
    categories_detail_api_view,
    categories_list_api_view, 
    products_detail_api_view, 
    products_list_api_view,
    reviews_detail_api_view,
    reviews_list_api_view)

producturlpatterns = [
    path('api/v1/products/', products_list_api_view),
    path('api/v1/products/<int:product_id>', products_detail_api_view),
    path('api/v1/categories/', categories_list_api_view),
    path('api/v1/categories/<int:category_id>', categories_detail_api_view),
    path('api/v1/reviews/', reviews_list_api_view),
    path('api/v1/reviews/<int:review_id>', reviews_detail_api_view)
]

urlpatterns = producturlpatterns + [
    path('admin/', admin.site.urls),
]
