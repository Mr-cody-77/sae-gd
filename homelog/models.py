from django.db import models

# Create your models here.

class registered(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=100, unique=True)
    dept = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    

