from django.db import models
import datetime
from django.contrib.auth.models import User
from account.models import UserProfile
# Create your models here.

LIKE_CHOICES=(
    ('LIKE','like'),
    ('UNLIKE','unlike'),
)
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)

    contain=models.TextField(max_length=400 ,null=True) 
    image=models.ImageField(upload_to='images/postimage',default="",blank=True,null=True)
    liked=models.ManyToManyField(User,blank=True, related_name='like')
    created=models.DateTimeField(auto_now_add=True) 
    # updated =
    

    def __str__(self):
        return self.contain 

    @property
    def likes_count(self):
        return self.liked.count()

class Comment(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    profile=models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True, blank=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True, blank=True)
    comment=models.TextField(max_length=200,blank=True,null=True)
    reply=models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name="replies")
    date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.comment)


class Likes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True, blank=True)
    value=models.CharField(choices=LIKE_CHOICES, default='LIKE',max_length=10)

