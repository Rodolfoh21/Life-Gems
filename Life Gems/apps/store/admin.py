from django.contrib import admin
from .models.brand import Brands
from .models.category import Category
from .models.product import Product, Inventory
from .models.orders import Order, OrderItem, ShippingAddress
from .models.subcategory import SubCategory
from .models.customer import Customer

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['ID', 'Name']

class SubCategoryAdmin(admin.ModelAdmin):
  list_display = ['Category', 'Name']

class BrandAdmin(admin.ModelAdmin):
  list_display = ['Name']
class ProductAdmin(admin.ModelAdmin):
  list_display = ['Category', 'SubCategory', 'Name', 'Price', 'Quantity']

class InventoryAdmin(admin.ModelAdmin):
  list_display = ['ID', 'Name', 'Quantity', 'Availability']

admin.site.register(Customer)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Brands, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)