from django.db import models
from ..models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='restaurant')

    def __str__(self):
        return self.name 
