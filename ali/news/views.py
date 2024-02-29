from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.


def home(request):
   info= CompanyInformation.objects.all().first()
   products= Product.objects.all()

   data={
        'info':info,
        'products':products
   }
   
   return render(request,'home.html',data)
   

def about(request):
   return render(request,'about.html')
   
def contact(request):
   if request.method =='POST':
      user_name  = request.POST.get('name')
      user_email  = request.POST.get('email')
      user_text  = request.POST.get('text')
   
      obj = ContactInfo()
      
      obj.name = user_name
      obj.email =user_email
      obj.text = user_text
      obj.save()
   return render(request, 'contact.html')