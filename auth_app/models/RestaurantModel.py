from django.db import models
from django.urls import reverse

# Create your models here.

class Restaurant(models.Model):
    code = models.CharField(max_length=50, null=False, blank=False, primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    cellphone = models.CharField(max_length=100, blank=False,null=False)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=False, null=False)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Code : {} , Name : {}, Address : {}, Phone : {}, Cellphone : {}".format(
            self.code,
            self.name,
            self.cellphone,
            self.phone,
            self.address
        )

    def get_absolute_url(self):
        return reverse("auth_app:restaurant_details", kwargs={"code": self.code})

    class Meta:
        db_table = "Restaurant"