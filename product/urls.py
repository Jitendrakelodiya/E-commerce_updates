from django.urls import path
from .views import *

urlpatterns = [

    # path('electronics',Electronics,name="Electronics"),
    # path('groceries',Groceries,name="Groceries"),
    # path('clothes',Clothes,name="Cloths"),
    # path('home&kitchen',Home_Kitchen,name="Home_Kitchen"),
    path('product_all/<str:pname>',Product,name="product_all"),
    path('common/',Common,name="common"),
    path('seller_base/',Seller_base,name="seller_base"),
    path('add-to-cart/<str:card>/',add_to_cart,name="add_to_cart"),
]