from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Booking(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
