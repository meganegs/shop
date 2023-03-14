from django.contrib import admin

# Register your models here.

from boutique.models import Product, Category


admin.site.register(Product )
admin.site.register(Category )

