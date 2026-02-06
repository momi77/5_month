from django.db import models

from users.models import CustomUser
from common.models import BaseModel



class CategoryModel(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"

class ProductModel(BaseModel ):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.title} - {self.price}"
    
class ReviewModel(models.Model):
    text = models.TextField()
    star = models.IntegerField(choices=((i, i) for i in range(1, 6)), default=5)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='reviews')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.product}"
