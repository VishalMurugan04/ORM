from django.db import models
from django.contrib import admin 
class blinkit(models.Model):
    SNumber=models.IntegerField()
    Name=models.CharField(max_length=10)
    Address=models.TextField()
    Productname=models.CharField(max_length=10)
    Quantity=models.IntegerField()
    price=models.IntegerField()
    Type=models.CharField()
    Mobile_Number=models.IntegerField(primary_key=True)
class blinkitadmin(admin.ModelAdmin):
    list_display=["SNumber","Name","Address","Productname","Quantity","price","Type","Mobile_Number"]
