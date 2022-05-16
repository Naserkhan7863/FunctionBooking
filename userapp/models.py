from django.db import models

# Create your models here.
class UserDetailsModel(models.Model):


     user_id=models.AutoField(primary_key=True)
     name=models.CharField(max_length=100,help_text="Enter FullName")
     email=models.EmailField(max_length=100,help_text="Enter Email id")
     contact=models.BigIntegerField(help_text="Enter Mobile Number" ,null=True)
     password=models.CharField(max_length=100,help_text="Enter Password")


     def __str__(self):
         return self.email
         
     
     class Meta:
         db_table="user_details"
    


class UserFeedbackModel(models.Model):


     feedback_id=models.AutoField(primary_key=True)
     type=models.CharField(max_length=100,help_text="Enter FullName")
     feedback=models.CharField(max_length=100,help_text="Enter Password")


     def __str__(self):
         return self.type
         
     
     class Meta:
         db_table="feedback_details"
    