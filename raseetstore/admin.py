from django.contrib import admin
from . models import product, category, sub_category, about_product
# Register your models here.

admin.site.register(sub_category)
admin.site.register(category)
admin.site.register(product)
admin.site.register(about_product)
