from django.shortcuts import render, redirect
# from .models import Elec_Product
from .models import *
from accounts.views import *
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
# @login_required(login_url="login")
# def Groceries(request):
#     Grocery_data = Groceries_Product.objects.all()
#     data = {
#         "Grocery_data" : Grocery_data
#     }
#     return render(request,"products/groceries.html",data)

# # @login_required(login_url="login")
# def Clothes(request):
#     Cloth_data = Cloth_Product.objects.all()
#     data = {
#         "Cloth_data" : Cloth_data
#     }
#     return render(request,"products/clothes.html",data)


# def Home_Kitchen(request):
#     H_K_data = H_K_Product.objects.all()
#     data = {
#         "H_K_data" : H_K_data
#     }
#     return render(request,"products/home_kitchen.html",data)


# def Electronics(request):
#     # Elec_data = Elec_Product.objects.all()
#     # data = {
#     #     "Elec_data" : Elec_data
#     # }
#         pass

def Seller_base(request):
    return render(request,"products/seller_base.html")



# @login_required(login_url="login")
def Common(request):
    categories = Category_shop.objects.all()
    # print("==========================================================")
    main = request.user
    # categories1 = Category_shop.objects.get(category =  pname)
    # mydata = Product_shop.objects.filter(category_id =categories1.id)
    # for i in mydata:
    #     print(i.product_name)
    if request.method == "POST": 
        category1 = request.POST.get('Category')
        cat = Category_shop.objects.get(category = category1)
        print(cat)
        product_name = request.POST.get('product_name')
        print(product_name)
        product_price = request.POST.get('product_price')
        print(product_price)
        product_desc = request.POST.get('product_desc')
        print(product_desc)
        pub_date = request.POST.get('pub_date')
        print(pub_date)
        product_image = request.FILES['product_image']
        print(product_image)
        prod_quintity = request.POST.get('prod_quintity')

        data = Products_shop(
            category = cat,
            product_name = product_name,
            product_price = product_price,
            product_desc = product_desc,
            pub_date = pub_date,
            product_image = product_image,
            prod_quintity = prod_quintity,
            user_id =main.id
        )
        
        data.save()
    
    
    context = {
        "categories":categories
    }

    return render(request,"products/common.html",context)

def Product(request , pname):
    categories1 = Category_shop.objects.get(category =  pname)
    Prod_data = Products_shop.objects.filter(category_id =categories1.id)


    categories = Category_shop.objects.all()
    context = {
               "categories":categories,
               "Prod_data" : Prod_data,

                       }

    return render(request,"products/product.html",context)


def add_to_cart(request, card):
    # categories1 = Category_shop.objects.get(category =  pname)
    # Prod_data = Product_shop.objects.filter(category_id =categories1.id)
    product = Product_shop.objects.get(product_name = card)
    print("-------------------------------------")
    print(product)
    user = request.user  
    print(user)
    # cart , _ = Cart_Item.objects.get_or_create(user = user , is_paid =False ,)
    
    cart_item =Cart_Item.objects.create(user=user,is_paid = False,  product= product)
    cart_item.save()
    return redirect("/")
