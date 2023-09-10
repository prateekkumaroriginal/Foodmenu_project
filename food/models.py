from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Food(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.CharField(max_length=500, default="https://wickedwhiskricelake.com/wp-content/uploads/2023/04/EmptyDinnerPlates.jpg")

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("food:food-details", kwargs={"item_id": self.pk})
    