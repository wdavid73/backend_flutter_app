from django.db import models
from django.urls import reverse


class Restaurant(models.Model):
    code = models.CharField(max_length=50, null=False,
                            blank=True, primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    cellphone = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=False, null=False)
    state = models.SmallIntegerField(default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Restaurant : {}, Code : {} , Address : {}, Phone : {}, Cellphone : {}".format(
            self.name,
            self.code,
             self.address,
             self.phone,
            self.cellphone,
        )

    def get_absolute_url(self):
        return reverse("auth_app:restaurant_details", kwargs={"code": self.code})

    class Meta:
        db_table = "Restaurant"
