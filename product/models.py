from django.db import models
from django.utils.text import slugify
# from autoslug import AutoSlugField
from accounts.models import User
# from product.models import Product_shop


    
class Category_shop(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category
    
# class Product_shop(models.Model):
#     category = models.ForeignKey(Category_shop, on_delete=models.CASCADE)
#     product_name = models.CharField( max_length=50)
#     product_price = models.CharField(max_length=20)
#     product_desc = models.CharField(max_length=500)
#     pub_date = models.DateField(auto_now_add=True)
#     product_image = models.ImageField(upload_to="media/static/images", null=True)
#     prod_quintity = models.PositiveIntegerField(null=True,blank=True)
#     mark = models.BooleanField(default=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    # elec_slug = AutoSlugField(populate_from='product_name',unique=True,null=True,default=None)

class Products_shop(models.Model):
        category = models.ForeignKey(Category_shop, on_delete=models.CASCADE)
        product_name = models.CharField( max_length=50)
        product_price = models.CharField(max_length=20)
        product_desc = models.CharField(max_length=500)
        pub_date = models.DateField(auto_now_add=True)
        product_image = models.ImageField(upload_to="media/static/images", null=True)
        prod_quintity = models.PositiveIntegerField(null=True,blank=True)
        mark = models.BooleanField(default=False)
        user = models.ForeignKey(User, on_delete=models.CASCADE)


        def __str__(self):
            return self.product_name


# Create your models here.
# class Cart(models.Model):
    

# class CartItem(models.Model):
#     user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='carts')
#     is_paid = models.BooleanField(default=False)
#     # cart = models.ForeignKey(on_delete=models.CASCADE , related_name="cart_items")
#     # product = models.ForeignKey(Product_shop, on_delete=models.CASCADE  )

# class Cart_Item(models.Model):
#     user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='carts')
#     is_paid = models.BooleanField(default=False)
#     # cart = models.ForeignKey(on_delete=models.CASCADE , related_name="cart_items")
#     product = models.ForeignKey(Product_shop, on_delete=models.CASCADE  )


class Cart_product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='carts')
    is_paid = models.BooleanField(default=False)

