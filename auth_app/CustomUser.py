from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from .Position.models.PositionModel import Position
from .Restaurant.models.RestaurantModel import Restaurant


class CustomUserManager(UserManager):
    def create_user(self, username, email, password, first_name, last_name, phone, restaurant, position):
        """
        Create and save a user with the given username, email, password, first_name, last_name , phone, restaurant_code, position_id.
        """
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name,
                          phone=phone, restaurant=restaurant, position=position)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=100, blank=False, null=False, unique=True,
        error_messages={'unique': 'Please use another username'},
        validators=[username_validator])
    email = models.EmailField(
        max_length=100, blank=False, null=False, unique=True,
        error_messages={'unique': 'Please use another email for this user'})
    password = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=100, blank=False, null=False)
    state = models.SmallIntegerField(default=1, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE,
                                 null=True, related_name='%(app_label)s_%(class)s_related'
                                 )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   db_column='restaurant_code', null=True,
                                   related_name='%(app_label)s_%(class)s_related'
                                   )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    def get_email_field(self):
        return self.email

    def get_restaurant(self):
        return self.restaurant

    def __str__(self):
        return "{} - {} - {} {} - {} - {} | {} - {}".format(self.pk, self.username, self.first_name, self.last_name,
                                                            self.email, self.phone, self.position, self.restaurant)

    objects = CustomUserManager()

    class Meta:
        db_table = "AuthUser"
