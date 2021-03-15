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

class PostComment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    userpost=models.ForeignKey(UserPost,on_delete=models.CASCADE,null=True, blank=True)
    comment=models.TextField(max_length=200,blank=True,null=True)
    commentreply=models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name="replies")
    commentdate=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.comment)