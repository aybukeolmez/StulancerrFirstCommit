from datetime import date
from django.db import models
from django.urls import reverse
from tinymce import models as tinycme_models
from autoslug import AutoSlugField
from django.contrib.auth.models import User


# Create your models here.

class AllUser(models.Model):
    all_user =models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    all_user_first_name = models.CharField(max_length=200)
    all_user_last_name =  models.CharField(max_length=200)
    all_user_user_name = models.CharField(max_length=200)
    all_user_email_adress =  models.CharField(max_length=200)
    all_user_password = models.CharField(max_length=200)

    normal_user_avatar = models.ImageField(upload_to='avatar')

    def __str__(self):
        return self.all_user_first_name + " "+self.all_user_last_name 


class Freelancer(models.Model):
    freelancer = models.ForeignKey(AllUser,on_delete=models.CASCADE,null=True)
    freelancer_first_name = models.CharField(max_length=200) 
    freelancer_last_name = models.CharField(max_length=200)
    freelancer_user_name = models.CharField(max_length=200)
    freelancer_email_address = models.CharField(max_length=200)
    freelancer_password = models.CharField(max_length=200)
    
    
    freelancer_avatar = models.ImageField(upload_to='freelancer_avatar')
    
    def __str__(self):
        return self.freelancer_first_name + " "+self.freelancer_last_name 
