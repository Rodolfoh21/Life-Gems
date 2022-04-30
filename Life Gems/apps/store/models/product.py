from .brand import Brands
from .category import Category
from django.db import models
from .subcategory import SubCategory


class Product(models.Model):
    Category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True
    )
    Sub_Category = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        null=True
    )
    Brand = models.ForeignKey(
        Brands,
        on_delete=models.CASCADE,
        null=True
    )
    product_id = models.SmallAutoField(primary_key=True, null=False)
    product_name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    base_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False
    )
    image = models.ImageField(
        upload_to='static/uploads/products',
        blank=True,
        null=True
    )

    @property
    def foo(self):
        return self._foo

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        else:
            return url
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products_by_categoryid(cat_id):
        if cat_id:
            return Product.objects.filter(category=cat_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_all_products_by_subcategoryid(sub_id):
        if sub_id:
            return Product.objects.filter(subcategory=sub_id)
        else:
            return Product.get_all_products()

    class Meta:
        verbose_name_plural = "Products"
        db_table = "Products"

    def __str__(self):
        return self.product_name


class Inventory(models.Model):
    Inventory_ID = models.SmallAutoField(
        primary_key=True,
        unique=True,
        null=False
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    qty = models.IntegerField(null=False, blank=False, default=0)
    available = models.BooleanField(null=False, default=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_all_Inventory_items():
        return Inventory.objects.all()

    @staticmethod
    def get_item_quantity(self):
        return str(self.qty)

    @staticmethod
    def check_item_availability(self):
        return str(self.available)

    class Meta:
        verbose_name_plural = "Inventory List"

    def __str__(self):
        return str(self.Inventory_ID)
