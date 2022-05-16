from django.shortcuts import render,redirect
from mainapp.models import ServiceDetailsModel
from banquetapp.models import BanquetProfileModel
# Create your views here.
def index(request):
  data=ServiceDetailsModel.objects.all()

  
  return render(request,'main/index.html',{"data":data})

def about(request):
  return render(request,'main/about.html')

def contact(request):
  return render(request,'main/contact.html')

def function_halls(request):
  function_halls=BanquetProfileModel.objects.all()

  return render(request,'main/function-halls.html',{"function_halls":function_halls})

def services(request):
  if request.method == "POST" and request.FILES['image']:
        service_type= request.POST.get('service_type')
        org = request.POST.get('org')
        price = request.POST.get('price')
        image = request.FILES['image']
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        description = request.POST.get('description')

        ServiceDetailsModel.objects.create(service_type=service_type,org=org,email=email,contact=contact,price=price,description=description,image=image)
  return render(request,'main/services.html')
