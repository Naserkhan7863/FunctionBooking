from django.db import models

# Create your models here.
class ServiceDetailsModel(models.Model):


     service_id=models.AutoField(primary_key=True)
     service_type=models.CharField(max_length=100,help_text="Enter FullName")
     org=models.CharField(max_length=100,help_text="Enter Email id")
     price=models.IntegerField(help_text="Enter Mobile Number" ,null=True)
     image=models.ImageField(upload_to='images/' ,null=True)
     contact=models.BigIntegerField(help_text="Enter Mobile Number" ,null=True)
     email=models.EmailField(help_text="Enter Mobile Number" ,null=True)
     description=models.TextField(help_text="Enter Mobile Number" ,null=True)
     service_status=models.CharField(max_length=100,default="pending",help_text="Enter Email id",null=True)

     def __str__(self):
         return self.service_type
         
     
     class Meta:
         db_table="service_details"
    
