from django.db import models
from django.contrib.auth.models import User

gender_choices=(
   ( 'm','male'),
   ( 'fm','female'),
   ( 'o','other')
)


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, blank=True)
    dob=models.DateField(null=True)
    gender=models.CharField(max_length=10,choices=gender_choices)
    profile_pic=models.ImageField(upload_to="images/profile"
    ,default="images/profile/profile-default.png" )
    profile_cover=models.ImageField(upload_to="images/coverimage"
    ,default="images/coverimage/cover-def.png")
    friends=models.ManyToManyField(User,blank=True,related_name="friends",null=True)

    def __str__(self):
        return self.user.username


class FriendRequest(models.Model):
    request_sender=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="sender")
    request_accepter=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="accepter")
    
    def __str__(self):
        return self.request_sender.username

