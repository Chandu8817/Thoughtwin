from django.db import models
import datetime
from django.contrib.auth.models import User
from account.models import UserProfile
# Create your models here.

class UserPost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)

    postcontain=models.TextField(max_length=400 ,null=True) 
    postimage=models.ImageField(upload_to='images/postimage')
    dateofpost=models.DateTimeField(auto_now_add=True) 
    

    def __str__(self):
        return self.postcontain 

class LikesnComments(models.Model):
    userpost=models.ManyToManyField(UserPost,null=True,blank=True)
    comments=models.TextField(max_length=200,blank=True,null=True)
    likes=models.IntegerField(default=0,blank=True,null=True)