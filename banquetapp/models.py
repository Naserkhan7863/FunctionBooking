from django.db import models

# Create your models here.
class BanquetDetailsModel(models.Model):


     user_id=models.AutoField(primary_key=True)
     name=models.CharField(max_length=100,help_text="Enter FullName")
     email=models.EmailField(max_length=100,help_text="Enter Email id")
     contact=models.BigIntegerField(help_text="Enter Mobile Number" ,null=True)
     password=models.CharField(max_length=100,help_text="Enter Password")
     banquet_status=models.CharField(max_length=100,default="pending",help_text="Enter FullName")


     def __str__(self):
         return self.email
         
     
     class Meta:
         db_table="banquet_details"
    



class BanquetProfileModel(models.Model):


     profile_id=models.AutoField(primary_key=True)
     user_id=models.ForeignKey(BanquetDetailsModel,db_column="user_id", on_delete=models.CASCADE,null=True)

     venue_category=models.CharField(max_length=100,help_text="Enter FullName")
     venue_location=models.CharField(max_length=100,help_text="Enter FullName")
     name=models.CharField(max_length=100,help_text="Enter FullName")
     contact=models.BigIntegerField()
     price=models.IntegerField(help_text="Enter Mobile Number" ,null=True)
     year_built=models.IntegerField(help_text="Enter Mobile Number" ,null=True)
     seating_capacity=models.IntegerField(help_text="Enter Mobile Number" ,null=True)
     bathrooms=models.IntegerField(help_text="Enter Mobile Number" ,null=True)
     two_parking_area=models.IntegerField(help_text="Enter Mobile Number" ,null=True)
     four_parking_area=models.IntegerField(help_text="Enter Mobile Number" ,null=True)
     super_buildup_area=models.IntegerField(help_text="Enter Mobile Number" ,null=True)
     carpet_area=models.IntegerField(help_text="Enter Mobile Number" ,null=True)
     non_veg_plate=models.IntegerField(help_text="Enter Mobile Number" ,null=True)
     total_floors=models.IntegerField( null=True)
     first_image=models.ImageField(upload_to='images/' ,null=True)
     second_imagee=models.ImageField(upload_to='images/' ,null=True)
     third_imageee=models.ImageField(upload_to='images/' ,null=True)
     fourth_image=models.ImageField(upload_to='images/' ,null=True)
     dj=models.CharField(max_length=100,help_text="Enter FullName")
     deco=models.CharField(max_length=100,help_text="Enter FullName")
     catering=models.CharField(max_length=100,help_text="Enter FullName")
     room=models.CharField(max_length=100,help_text="Enter FullName")
     music=models.CharField(max_length=100,help_text="Enter FullName")
     crackers=models.CharField(max_length=100,help_text="Enter FullName")
     description=models.TextField(help_text="Enter FullName")
     address=models.CharField(max_length=100,help_text="Enter FullName")
     map=models.TextField(help_text="Enter FullName", null=True)


     def __str__(self):
         return self.email
         
     
     class Meta:
         db_table="banquet_profile_details"
    



class BanquetBookingModel(models.Model):


     booking_id=models.AutoField(primary_key=True)
     profile_id=models.ForeignKey(BanquetProfileModel,db_column="profile_id", on_delete=models.CASCADE,null=True)
     occasion=models.CharField(max_length=100,help_text="Enter FullName")
     date=models.DateField(max_length=100,help_text="Enter FullName")
     time=models.TimeField(max_length=100,help_text="Enter FullName")
     contact=models.BigIntegerField()
     price=models.IntegerField(help_text="Enter Mobile Number" ,null=True)
     guest=models.IntegerField(help_text="Enter Mobile Number" ,null=True)
     groom=models.CharField(max_length=100,help_text="Enter FullName")
     bride=models.CharField(max_length=100,help_text="Enter FullName")
     deco=models.CharField(max_length=100,help_text="Enter FullName")
     serving=models.CharField(max_length=100,help_text="Enter FullName")
     plate_price=models.IntegerField(help_text="Enter FullName")
     user=models.CharField(max_length=100,help_text="Enter FullName")
     advance=models.IntegerField(help_text="Enter Mobile Number" ,null=True)
     services=models.CharField(max_length=100,null=True)
     description=models.TextField(help_text="Enter FullName")
     address=models.CharField(max_length=100,help_text="Enter FullName")


     def __str__(self):
         return self.booking_id
         
     
     class Meta:
         db_table="banquet_booking_details"
    