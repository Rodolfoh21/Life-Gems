from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(
        _('email address'),
        primary_key=True,
        unique=True,
        null=False,
    )
    password = models.CharField(max_length=50, null=False)
    phone_no = models.CharField(max_length=20, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Customers'

    def register(self):
        self.save()

    def __str__(self):
        return self.email

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def emailExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
