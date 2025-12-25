from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

class ProductModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} - {self.price}"

class ReviewModel(models.Model):
    text = models.CharField(max_length=500)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.product}"