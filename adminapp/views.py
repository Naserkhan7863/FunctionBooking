from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render
from mainapp.models import ServiceDetailsModel

from userapp.models import UserDetailsModel, UserFeedbackModel
from banquetapp.models import BanquetProfileModel,BanquetBookingModel
# Create your views here.
def admin_login(request):
     if request.method == "POST":
        name= request.POST.get('email')
        password= request.POST.get('password')
        if name =='admin' and password =='admin':
            return redirect('admin_dashboard')
        elif name =='fazal' and password =='fazal':
            return redirect('admin_dashboard')
  
     return render(request,'admin/admin-login.html')

def admin_dashboard(request):
     data=UserDetailsModel.objects.count()
     data1=BanquetBookingModel.objects.count()
     data2=BanquetProfileModel.objects.count()
     data3=ServiceDetailsModel.objects.count()
     return render(request,'admin/admin-dashboard.html',{"data":data,"data1":data1,"data2":data2,"data3":data3})

def admin_function_halls(request):
     data=BanquetProfileModel.objects.all()
     return render(request,'admin/admin-function-halls.html',{"data":data})

def function_halls_accept(request,id):
    accept=get_object_or_404(BanquetProfileModel,profile_id=id)
    accept.banquet_status='accept'
    accept.save(update_fields=['banquet_status'])
    accept.save()
    return redirect('admin_function_halls')

def function_halls_reject(request,id):
    reject=get_object_or_404(BanquetProfileModel,profile_id=id)
    reject.banquet_status='reject'
    reject.save(update_fields=['banquet_status'])
    reject.save()
    return redirect('admin_function_halls')

def admin_view_services(request):
     data=ServiceDetailsModel.objects.filter(service_status='pending')

     return render(request,'admin/admin-view-services.html',{"data":data})

def service_partners_accept(request,id):
    accept=get_object_or_404(ServiceDetailsModel,service_id=id)
    accept.service_status='accept'
    accept.save(update_fields=['service_status'])
    accept.save()
    return redirect('admin_view_services')

def service_partners_reject(request,id):
    reject=get_object_or_404(ServiceDetailsModel,service_id=id)
    reject.service_status='reject'
    reject.save(update_fields=['service_status'])
    reject.save()
    return redirect('admin_view_services')

def admin_view_users(request):
     data=UserDetailsModel.objects.all()
     return render(request,'admin/admin-view-users.html',{"data":data})

def admin_view_feedbacks(request):
     data=UserFeedbackModel.objects.all()
     return render(request,'admin/admin-view-feedback.html',{"data":data})