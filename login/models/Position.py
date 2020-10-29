from django.db import models
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    state = models.SmallIntegerField(default=1,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Position : {}".format(self.name)

    def get_absolute_url(self):
        return reverse("login:position_details", kwargs={"id": self.id})

    class Meta:
        db_table = "Restaurant"
    