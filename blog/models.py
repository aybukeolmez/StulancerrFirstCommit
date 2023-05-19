from datetime import date
from django.db import models
from django.urls import reverse
from tinymce import models as tinycme_models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

from slugify import slugify

class BaseModel(models.Model):
    title =models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title',unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    def __str__(self):
        return self.title
    



class Post(BaseModel):
    free_user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    cover_image = models.ImageField(upload_to='post')
    content = tinycme_models.HTMLField(blank=True,null=True)

    def __str__(self):
        return self.title 






    














































# Create your models here.
# class BaseModel(models.Model):
#     title = models.CharField(max_length=200)
#     slug = AutoSlugField(populate_from='title',unique=True)
#     is_active = models.BooleanField(default=False)
#     created_at =models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True


# class Category(BaseModel):
#     def __str__(self):
#         return self.title
    
# class Tag(BaseModel):
#     def __str__(self):
#         return self.title

# class Post(BaseModel):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
#     tag = models.ManyToManyField(Tag)
#     cover_image = models.ImageField(upload_to='post')
#     content = tinycme_models.HTMLField(blank=True,null=True)
#     view_count = models.PositiveBigIntegerField(default=0)
    

#     def __str__(self):
#         return self.title



# class Blog(models.Model):
#     author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Öğrenci")
#     title = models.CharField(max_length=50,verbose_name="Başlık")
#     content = models.TextField(verbose_name="İçerik")
#     created_at = models.DateTimeField(auto_now=True,verbose_name="Oluşturulma Tarihi")

#     def __str__(self):
#         return self.title
    


# class Freelancer(models.Model):
#     freelancer_name = models.CharField(max_length=200)
#     freelancer_surname = models.CharField(max_length=200)
#     register_date = models.DateTimeField("date published")    

#     def __str__(self):
#         return self.freelancer_name +" "+ self.freelancer_surname
