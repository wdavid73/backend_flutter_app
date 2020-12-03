from django.db import models
from django.urls import reverse
from auth_app.Restaurant.models.RestaurantModel import Restaurant

types = [
    ('BreakFast', 'BreakFast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),
    ('Dessert', 'Dessert'),
]


units = [
    ('gr', 'gr'),
    ('oz', 'oz'),
]


class Ingredient(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    quantity = models.IntegerField(null=False, blank=False)
    unit = models.CharField(max_length=100, blank=False,
                            null=False, choices=units)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Dish(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    type = models.CharField(max_length=100, blank=False,
                            null=False, choices=types)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   db_column='restaurant_code', null=True,
                                   related_name='%(app_label)s_%(class)s_related'
                                   )
    ingredient = models.ManyToManyField(Ingredient, through="Dish_Ingredient")
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Dish {} , {}, ${} ({}) ".format(self.pk, self.name, self.price, self.type)

    def get_absolute_url(self):
        return reverse("api_admin:dish_details", kwargs={"code": self.pk})

    class Meta:
        db_table = "Dish"


class Dish_Ingredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Dish : {} - Ingredient {}".format(self.dish, self.ingredient)

    class Meta:
        db_table = "Dish_Ingredient"
