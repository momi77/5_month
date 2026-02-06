from django.contrib import admin
from product.models import CategoryModel, ProductModel, ReviewModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = 'title price category owner created_at'.split()

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = 'name created_at'.split()
@admin.register(ReviewModel)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = 'text product'.split()

