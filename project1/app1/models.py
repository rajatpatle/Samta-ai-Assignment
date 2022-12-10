from django.db import models

# Create your models here.


class Data(models.Model):
    order_date = models.DateField()
    region = models.CharField(max_length=50)
    manager = models.CharField(max_length=50)
    salesman = models.CharField(max_length=50)
    items = models.CharField(max_length=50)
    units = models.IntegerField()

    def __str__(self):
        return self.salesman
