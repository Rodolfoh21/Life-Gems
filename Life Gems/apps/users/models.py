from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
import uuid


class Customer(AbstractUser):
    user_role_choices = [
        ('RC', 'Regular Chad'),
        ('PC', 'Primo Sigma'),
        ('AD', 'Administrator'),
    ]
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user_role = models.CharField(
        max_length=2,
        choices=user_role_choices,
        default=user_role_choices[0][0]
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
        null=False
    )
    first_name = models.Charfield(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    phone_no = models.CharField(max_length=10, null=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.first_name
