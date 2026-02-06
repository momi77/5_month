
from django.contrib import admin
from django.urls import path, include
from product.views import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoriesListAPIView,
    CategoryDetailAPIView,
    ReviewsListAPIView,
    ReviewsDetailAPIView,
)

from . import swagger
from product.views import ReviewsDetailAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from users.views import CustomTokenObtainPairView

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
    path('api/v1/', include('product.urls')),
    path('api/v1/users/', include('users.urls')),

    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]


urlpatterns += swagger.urlpatterns

urlpatterns += [
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]