from django.db import models
from ..models import User
from .restaurant import Restaurant

class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dateTime = models.DateTimeField()
