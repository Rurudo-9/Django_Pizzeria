import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza, Topping

Pizzas = Pizza.objects.all()

p = Pizza.objects.get(id=1)

print(p)

Toppings = p.topping_set.all()

for topping in Toppings:
    print(topping)

'''
for p in Pizzas:
    print(f"Pizza ID: {p.id} Pizza: {p}")

Toppings = Topping.objects.all()

for t in Toppings:
    print(f"Pizza: {t.pizza}")
    print(f"Topping: {t.name}")

'''


