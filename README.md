# Ex02 Django ORM Web Application
## Date:10.10.2026

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
'''
models.py
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

admin.py
from django.contrib import admin
from .models import Tomato,TomatoAdmin
admin.site.register(Tomato,TomatoAdmin)

'''


## OUTPUT



## RESULT
Thus the program for creating vehicle service Database using ORM hss been executed successfully.
