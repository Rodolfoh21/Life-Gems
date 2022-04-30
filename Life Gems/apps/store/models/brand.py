from django.db import models


class Brands(models.Model):
    brand_name = models.CharField(max_length=20, null=False, unique=True)
    id = models.SmallAutoField(primary_key=True, null=False)

    @staticmethod
    def get_all_brands():
        return Brands.objects.all()

    class Meta:
        verbose_name_plural = "Brands"
        db_table = "Brands"

    def __str__(self):
        return self.brand_name
