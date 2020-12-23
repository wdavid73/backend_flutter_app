from django.db import models
from django.urls import reverse

from auth_app.Restaurant.models.RestaurantModel import Restaurant


class Drink(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=5000.00)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, db_column='restaurant_code', null=False)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - $ {} - {}".format(self.name, self.price, self.restaurant.code)

    class Meta:
        db_table = "Drink"
