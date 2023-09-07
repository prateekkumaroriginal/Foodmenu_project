from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.CharField(max_length=500, default="https://wickedwhiskricelake.com/wp-content/uploads/2023/04/EmptyDinnerPlates.jpg")

    def __str__(self):
        return self.name