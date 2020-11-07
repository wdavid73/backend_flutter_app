import uuid
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models, IntegrityError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .Position.models.PositionModel import Position
from .Restaurant.models.RestaurantModel import Restaurant


class CustomizedUserManager(UserManager):
    def get_or_create_for_auth_app(self, payload):
        auth_app_id = payload['sub']

        try:
            return self.get(auth_app_id=auth_app_id)
        except self.model.DoesNotExist:
            pass

        try:
            user = self.create(auth_app_id=auth_app_id,
                               email=payload['email'],
                               is_active=True)
        except IntegrityError:
            user = self.get(auth_app_id=auth_app_id)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 charaters of fewer . Letter , digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists.")
        }
    )

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)

    s_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    auth_app_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    objects = CustomizedUserManager()
