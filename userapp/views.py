import imp
import profile
from django.shortcuts import render,redirect
from userapp.models import UserDetailsModel,UserFeedbackModel
from mainapp.models import ServiceDetailsModel
# Create your views here.
from banquetapp.models import BanquetProfileModel,BanquetBookingModel


def user_register(request):

   if request.method == "POST":
        name= request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        
        UserDetailsModel.objects.create(name=name,email=email,contact=contact,password=password)
   return render(request,'user/user-register.html')

def user_login(request):

   if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            check=UserDetailsModel.objects.get(email=email,password=password)
            request.session["user_id"]=check.user_id
            return redirect("user_dashboard")
        except:
         pass
   return render(request,'user/user-login.html')


def user_dashboard(request):
     data=UserDetailsModel.objects.count()
     data1=BanquetBookingModel.objects.count()
     data2=BanquetProfileModel.objects.count()
     data3=ServiceDetailsModel.objects.count()
     return render(request,'user/user-dashboard.html',{"data":data,"data1":data1,"data2":data2,"data3":data3})

def user_functionhall(request):
    function_halls=BanquetProfileModel.objects.all()

    return render(request,'user/user-functionhall.html',{"function_halls":function_halls})

def user_functionhall_details(request,id):
      prod = BanquetProfileModel.objects.get(profile_id=id)
      prodd = BanquetProfileModel.objects.get(profile_id=id)
      prod2 = BanquetProfileModel.objects.exclude(profile_id=id)
      prod3 = BanquetBookingModel.objects.filter(booking_id=id)

      return render(request,'user/user-function-hall-details.html',{"prod":prod , "prodd":prodd , "prod2":prod2, "prod3":prod3})

def user_services(request):
 data=ServiceDetailsModel.objects.all()

 return render(request,'user/user-services.html',{"data":data})

def user_feedback(request):

     if request.method == "POST":
        type = request.POST.get('type')
        feedback = request.POST.get('feedback')
        
        UserFeedbackModel.objects.create(type=type,feedback=feedback)
     return render(request,'user/feedback.html')

