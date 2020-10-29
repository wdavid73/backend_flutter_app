from django.contrib.auth.models import AbstractUser
from django.db import models
from .PositionModel import Position
from .RestaurantModel import Restaurant


class User22(AbstractUser):
    username = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=32, null=False, blank=False)
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=100, blank=False, null=False)
    state = models.SmallIntegerField(default=1, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    restaurant_code = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'email', 'password']

    # def get_email_field_name(self):
    # return self.email

    # def get_full_name(self):
    # return self.first_name + self.last_name

    # def short_name(self):
    # return self.first_name + self.__dict__["last_name"][0].upper()+"."
