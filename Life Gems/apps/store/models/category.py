from django.db import models


class Category(models.Model):
    cat_id = models.SmallAutoField(primary_key=True, null=False)
    cat_name = models.CharField(max_length=20, null=False, unique=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "Categories"

    def __str__(self):
        return self.cat_name
