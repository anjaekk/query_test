from django.db import models
from django.db.models.fields.related import ManyToManyField


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cities'


class Owner(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'owners'


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'restaurants'


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    restaurant = ManyToManyField(Restaurant, related_name="pizzas")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pizzas'