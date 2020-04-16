from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=15, blank=False, null=False, unique=True)
    email = models.EmailField(_('email address'), blank=True, null=True, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_admin = models.BooleanField(blank=False, null=False, default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'USER'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return "{}".format(self.username)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return "{} {}".format(self.first_name, self.last_name)
