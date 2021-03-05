from django.db import models
from account.models import User,UserProfile
# Create your models here.

class UserPost(models.Model):
    post_description=models.CharField(max_length=250)
    post_image=models.ImageField(upload_to='images/postimages')
    post_user=models.ForeignKey(User, on_delete=models.CASCADE)
    post_time=models.DateTimeField('date published')


    def __str__(self):

        return self.post_description

    

class CommentsOnPost(models.Model):

    post_comment=models.ForeignKey(UserPost,on_delete=models.CASCADE)
    comment_user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.CharField(max_length=100 ,blank=True)
    comment_date=models.DateTimeField('date published')