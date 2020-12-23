from django.db import models
from django.urls import reverse

units = [
    ('gr', 'gr'),
    ('oz', 'oz'),
]


class Complement(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=5000.00)
    quantity = models.IntegerField(null=False, blank=False)
    unit = models.CharField(max_length=100, blank=False,
                            null=False, choices=units)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - $ {} - {} {}".format(self.name, self.price, self.quantity, self.unit)

    class Meta:
        db_table = "Complement"
