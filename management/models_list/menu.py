from django.db import models
from .restaurant import Restaurant
from django.core.validators import MinValueValidator

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    description = models.CharField(max_length=500)
    type = models.BooleanField()
    image = models.ImageField(upload_to='menu')

    class Meta:
        unique_together = ('restaurant', 'name')
        constraints = [
            models.CheckConstraint(check=models.Q(price__gt=0), name='min_price')
        ]
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['type'])
        ]

    def __str__(self):
        return self.name