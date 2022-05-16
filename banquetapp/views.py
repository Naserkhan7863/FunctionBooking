import profile
from django.shortcuts import render,redirect
from banquetapp.models import BanquetDetailsModel,BanquetProfileModel,BanquetBookingModel
from mainapp.models import ServiceDetailsModel
from userapp.models import UserDetailsModel
# Create your views here.


def banquet_register(request):

    if request.method == "POST":
        name= request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        
        BanquetDetailsModel.objects.create(name=name,email=email,contact=contact,password=password)
    return render(request,'banquet/banquet-register.html')

def banquet_login(request):
  if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            check=BanquetDetailsModel.objects.get(email=email,password=password)
            request.session["user_id"]=check.user_id
            return redirect("banquet_dashboard")
        except:
         pass
  return render(request,'banquet/banquet-login.html')

def banquet_dashboard(request):
  data=UserDetailsModel.objects.count()
  data1=BanquetBookingModel.objects.count()
  data2=BanquetProfileModel.objects.count()
  data3=ServiceDetailsModel.objects.count()

  return render(request,'banquet/banquet-dashboard.html',{"data":data,"data1":data1,"data2":data2,"data3":data3})

def banquet_add_profile(request):
  user_id=request.session["user_id"]

  if request.method == "POST" and request.FILES['first_image']  and request.FILES['second_imagee']  and request.FILES['third_imageee'] and request.FILES['fourth_image']:
        venue_category= request.POST.get('venue_category')
        venue_location = request.POST.get('venue_location')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        price = request.POST.get('price')
        year_built = request.POST.get('year_built')
        seating_capacity= request.POST.get('seating_capacity')
        bathrooms = request.POST.get('bathrooms')
        two_parking_area = request.POST.get('two_parking_area')
        four_parking_area = request.POST.get('four_parking_area')
        super_buildup_area = request.POST.get('super_buildup_area')
        carpet_area = request.POST.get('carpet_area')
        non_veg_plate = request.POST.get('non_veg_plate')
        total_floors = request.POST.get('total_floors')
        first_image = request.FILES['first_image']
        second_imagee = request.FILES['second_imagee']
        third_imageee= request.FILES['third_imageee']
        fourth_image = request.FILES['fourth_image']
        dj = request.POST.get('dj')
        deco = request.POST.get('deco')
        catering = request.POST.get('catering')
        room = request.POST.get('room')
        music = request.POST.get('music')
        crackers = request.POST.get('crackers')
        description = request.POST.get('description')
        address = request.POST.get('address')
        map = request.POST.get('map')

        user_id=BanquetDetailsModel.objects.get(user_id=user_id)
        BanquetProfileModel.objects.create(user_id=user_id,venue_category=venue_category,venue_location=venue_location,name=name,contact=contact,price=price,year_built=year_built,seating_capacity=seating_capacity,bathrooms=bathrooms,two_parking_area=two_parking_area,four_parking_area=four_parking_area,super_buildup_area=super_buildup_area,
        carpet_area=carpet_area,non_veg_plate=non_veg_plate,total_floors=total_floors,first_image=first_image,second_imagee=second_imagee,third_imageee=third_imageee,fourth_image=fourth_image,dj=dj,deco=deco,catering=catering,room=room,music=music,crackers=crackers,description=description,address=address,map=map)
  return render(request,'banquet/banquet-add-profile.html')

def banquet_add_booking(request):
    user_id = request.session['user_id']
    print("a")
    try:
        print("b")

        check = BanquetDetailsModel.objects.get(user_id = user_id)
        print("b")

        status = check.banquet_status
        print(status)
        if status=="reject":
            print("b")
            # messages.warning(request,"your account is Rejected")
            print("c")
            return redirect('banquet_dashboard')
            
        elif status == "accept":
          check = BanquetDetailsModel.objects.get(user_id = user_id)

          print("hiii")
          if request.method == "POST":
            print("post")
            occasion= request.POST.get('occasion')
            date = request.POST.get('date')
            time = request.POST.get('time')
            guest = request.POST.get('guest')
            groom = request.POST.get('groom')
            bride = request.POST.get('bride')
            price= request.POST.get('price')
            deco = request.POST.get('deco')
            serving = request.POST.get('serving')
            plate_price = request.POST.get('plate_price')
            user = request.POST.get('user')
            contact = request.POST.get('contact')
            advance = request.POST.get('advance')
            services = request.POST.get('services')
            description = request.POST.get('description')
            address = request.POST.get('address')
            print("aaaa")

            profile=BanquetProfileModel.objects.get(user_id=user_id)
            print(profile.profile_id)
            BanquetBookingModel.objects.create(profile_id=profile,occasion=occasion,date=date,time=time,contact=contact,price=price,guest=guest,groom=groom,deco=deco,serving=serving,bride=bride,plate_price=plate_price,user=user,
            services=services,advance=advance,description=description,address=address)
            return redirect('banquet_add_booking')
            
        elif status=="pending":
            print("rejecteddd")
            # messages.warning(request,"your account is in pending not activated")
            return redirect('banquet_dashboard')
    except Exception as ex:
        print(ex)
    return render(request,'banquet/add-booking.html')

def banquet_my_bookings(request):
  user_id=request.session["user_id"]

  booking_data=BanquetBookingModel.objects.filter(booking_id=user_id)
  return render(request,'banquet/my-bookings.html',{"booking_data":booking_data})


def banquet_feedbacks(request):
  return render(request,'banquet/feedback.html')

