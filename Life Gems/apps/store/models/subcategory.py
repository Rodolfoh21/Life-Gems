from django.db import models
from .category import Category

class SubCategory(models.Model):
    sub_id = models.SmallAutoField(primary_key=True, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=50, null=False, unique=True)
    
    @staticmethod
    def get_all_subcategories():
        return SubCategory.objects.all()
    
    class Meta:
        verbose_name_plural = "Sub Categories"
        db_table = "Subcategories"

    def __str__(self):
        return self.sub_name