from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.json import JSONField

# Create your models here.
class Compny_Details(models.Model):
    name=models.CharField(default="",max_length=200)
    email=models.EmailField(default="",max_length=200)
    number=models.CharField(default="",max_length=10)
    address=models.TextField(default="", max_length=200)
    join_date=models.DateField(auto_now=True,blank=True,null=True)
    profile=models.ImageField(upload_to="Profile/",max_length=300,default="",blank=True,null=True)
    password=models.CharField(default="",max_length=20)
    
class Compny_Customers(models.Model):
    comp=models.ForeignKey('Compny_Details',on_delete=models.CASCADE,blank=True,null=True)
    custName=models.CharField(default="",max_length=200)
    custMail=models.EmailField(default="",max_length=200)
    custCon=models.CharField(default="",max_length=200)
    custAdd=models.CharField(default="",max_length=200)
    custRgdate=models.DateTimeField(auto_now=True,blank=True,null=True)
    custProfile=models.ImageField(upload_to="Customer_Profile/",max_length=300,default="",blank=True,null=True)
    custPass=models.CharField(default="",max_length=20)
  
class Compny_Products(models.Model):
    comp=models.ForeignKey('Compny_Details',on_delete=models.CASCADE,blank=True,null=True)
    proName=models.CharField(default="",max_length=200)
    proPrice=models.PositiveBigIntegerField(default=0)
    proQnty=models.PositiveBigIntegerField(default=0)
    proImg=models.ImageField(upload_to="Product_Photos/",max_length=300,default="",blank=True,null=True)
    
class Customer_Order(models.Model):
    comp=models.ForeignKey('Compny_Details',on_delete=models.CASCADE,blank=True,null=True)
    cust=models.ForeignKey('Compny_Customers',on_delete=models.CASCADE,blank=True,null=True)
    prod=models.ForeignKey('Compny_Products',on_delete=models.CASCADE,blank=True,null=True)
    qty=models.PositiveBigIntegerField(default=0)
    total_price=models.PositiveBigIntegerField(default=0)
    order_date=models.DateTimeField(auto_now=True,blank=True,null=True)
    status=models.CharField(default="False",max_length=200)
    
class Customer_Feedback(models.Model):
    name=models.CharField(default='',max_length=100 )
    mail=models.EmailField(default="",max_length=200)    
    subject=models.CharField(default='',max_length=200)
    message=models.CharField(default='',max_length=200)
    date=models.DateTimeField(auto_now=True,blank=True,null=True)
