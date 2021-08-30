from restaurants.models import *
from django.db import connection


# selecte_related 미사용
restaurant = Restaurant.objects.get(id=1)
owner = restaurant.owner
city = owner.city
print(connection.queries)


# select_related 사용
restaurant = Restaurant.objects.select_related('owner__city').get(id=1)
owner = restaurant.owner
city = owner.city
print(connection.queries)


# prefetch_related 미사용
restaurants = Restaurant.objects.all()
for restaurant in restaurants:
    for pizza in restaurant.pizzas.all():
        print(restaurant.name+": "+pizza.name)
    print("")
print(connection.queries)


# prefetch_related 사용
restaurants = Restaurant.objects.all().prefetch_related('pizzas')
for restaurant in restaurants:
    for pizza in restaurant.pizzas.all():
        print(restaurant.name+": "+pizza.name)
    print("")
print(connection.queries)