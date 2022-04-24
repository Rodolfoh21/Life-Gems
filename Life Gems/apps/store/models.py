from django.db import models
from django.contrib.auth.models import AbstractUser


class Categories(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)
    id = models.SmallAutoField(primary_key=True, null=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SubCategories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, unique=True)
    id = models.SmallAutoField(primary_key=True, null=False)

    class Meta:
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.name


class Brands(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)
    id = models.SmallAutoField(primary_key=True, null=False)

    class Meta:
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.name


class Product(models.Model):
    Category = models.ForeignKey(Categories, on_delete=models.SET_NULL)
    Sub_Category = models.ForeignKey(SubCategories, on_delete=models.SET_NULL)
    Brand = models.ForeignKey(Brands, on_delete=models.CASCADE, null=False)
    id = models.SmallAutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField(max_length=100, null=False)
    image = models.ImageField(
        upload_to='static/img/',
        blank=True,
        null=True
    )
    description = models.TextField(null=True, blank=True)
