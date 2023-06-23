from django.contrib import admin

# Register your models here.
from .models import *



# admin.site.register(Elec_Product)
# admin.site.register(Groceries_Product)
# admin.site.register(H_K_Product)
# admin.site.register(Cloth_Product)

admin.site.register(Category_shop)

class ProductshopAdmin(admin.ModelAdmin):
    list_display = ("category","product_name","price","product_image")
admin.site.register(Products_shop)

admin.site.register(Cart_product)
# admin.site.register(Cart)


# class Category_typeAdmin(admin.ModelAdmin):
#     list_display = ('title','Catg_Name','status')
#     list_filter = ['status']

# class Product_typeAdmin(admin.ModelAdmin):
#     list_display = ('title','Catg_Name','status')
#     list_filter = ['status']

# admin.site.register(Category_type,Category_typeAdmin)
# admin.site.register(Product_type,Product_typeAdmin)
