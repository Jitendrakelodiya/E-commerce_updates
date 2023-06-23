from django.urls import path
from .views import *

urlpatterns = [
    path('Buyer_register/',Buyer_register,name="Buyer_register"),
    path('Seller_register/',Seller_register,name="Seller_register"),
    path('Buyer-Login/',Buyer_Login,name="Buyer_Login"),
    path('Seller-Login/',Seller_Login,name="Seller_Login"),
    path('user_logout/',Logout_page,name="user_logout"),
    
]