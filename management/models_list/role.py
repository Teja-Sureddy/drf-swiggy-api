from django.db import models

class Role(models.Model):
    ROLE_CHOICES = [
        ('admin', 'admin'),
        ('manager', 'manager'),
        ('user', 'user'),
    ]
    name = models.CharField(max_length=15, choices=ROLE_CHOICES, unique=True)   

    def __str__(self):
        return self.name