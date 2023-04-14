from django.db import models
from .order import Order
from .menu import Menu

class OrderedItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('order', 'item')