from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.






class Students(AbstractUser):
    RollNo=models.IntegerField(null=True,blank=True)
    Branch=models.CharField(max_length=100,null=True,blank=True)
    Image=models.FileField(null=True,blank=True)
    

    def __str__(self):
        return self.first_name
    

class Teacher(models.Model):
    
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.username

class Complaints(models.Model):
    user_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    #teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    complaint_name=models.CharField(max_length=50,null=True,blank=True)
    description=models.CharField(max_length=50,null=True,blank=True)
    reply=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.user_id.username    


      
    


        