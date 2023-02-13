from django.contrib import admin
# Register your models here.

from .models import Product
from .models import Category

admin.site.register(Category )



class Product(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['category']}),
        ('Titre', {'fields': ['Name']}),
        ('Category', {'fields': ['category']}),
        ('slug', {'fields': ['slug']}),
        ('Description', {'fields': ['description']}),
        ('Prix', {'fields': ['price']}),

    ]
   
admin.site.register(Product, Product)
