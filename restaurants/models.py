from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.OneToOneField("Restaurant", on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'owners'

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'restaurants'