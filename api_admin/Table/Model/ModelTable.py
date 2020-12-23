from django.db import models
from auth_app.Restaurant.models.RestaurantModel import Restaurant


class Table(models.Model):
    ref = models.CharField(max_length=100, null=False, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   db_column='restaurant_code', null=True)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Table {} - {} - {}".format(self.pk, self.ref, self.restaurant.code)

    class Meta:
        db_table = "Table"
