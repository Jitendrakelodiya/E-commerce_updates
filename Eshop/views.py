from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from product.models import Category_shop
from product.views import *


def Home(request):
  categories = Category_shop.objects.all()
  context = {
    "categories":categories
  }
  return render(request,"home.html",context)

# def (request):
#     return render(request,"about.html")

def ContactUs(request):
  if request.method == "POST":
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        print(email)
        number = request.POST.get('number')
        print(number)
        message = request.POST.get('message')
        print(message)

        content = {
          "name":name,
          "email": email,
          "number": number,
          "message": message
        }
        print(content)

        msg_plain = render_to_string('mail/mail.html',content)
        print(msg_plain)
            
        subject = "User information mail"
        # message1 = "hello how are you"
        send_mail(subject,msg_plain,'jitendra.kelodiya2020@gmail.com',["jitendra.kelodiya2020@gmail.com"],fail_silently=False)
        print("sent succesfully")
      
  categories = Category_shop.objects.all()
  context = {
        "categories":categories
        }
        
  return render(request,"contact.html",context)

def AboutUs(request):
  categories = Category_shop.objects.all()
  context = {
        "categories":categories
        }
  return render(request,"about.html",context)  

