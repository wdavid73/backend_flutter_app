from django.db import models
from django.urls import reverse

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

    def __str__(self):
        return "Ingredient {} - {} - {} {}".format(self.id, self.name, self.quantity, self.unit)

    class Meta:
        db_table = "Ingredient"
