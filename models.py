import datetime
from time import time
from django.contrib.auth.models import User
from django.db import models

depts = [('Mechanical Department','Mechanical Department'),('Civil Department','Civil Department'),('Computer Department','Computer Department'),
        ('Electrical Department','Electrical Department'),('Electronics and Telecommunication Department','Electronics and Telecommunication Department'),('Information Technology Department','Information Technology Department'),
        ('Data Science Department','Data Science Department'),('AI Department','AI Department')]

years = [('First Year','First Year'),('Second Year','Second Year'),('Third Year','Third Year'),
        ('Fourth Year','Fourth Year')]

class Profile(models.Model):
    prn_no = models.CharField(max_length = 13)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    date = models.DateField()
    phone = models.BigIntegerField()
    address = models.CharField(max_length=150)
    department = models.CharField(choices=depts,max_length=80,null=True,blank=False,default='Mechanical Department')
    year_of_study = models.CharField(choices=years,max_length=80,null=True,blank=False,default='First Year')
    detect = models.BooleanField(default=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face

class user_update(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.user)