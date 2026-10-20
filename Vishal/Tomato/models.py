from django.db import models
from django.contrib import admin
class Tomato(models.Model):
    SNumber=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=10)
    Phone_Number=models.IntegerField()
    Address=models.TextField()
    Product=models.CharField(max_length=10)
    Quantity=models.IntegerField()
    Brand=models.CharField(max_length=10)
    Price=models.IntegerField()
class TomatoAdmin(admin.ModelAdmin):
    list_display=["SNumber","Name","Phone_Number","Address","Product","Quantity","Brand","Price"]