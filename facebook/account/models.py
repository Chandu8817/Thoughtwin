from django.db import models

# Create your models here.

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
    profile_pic=models.ImageField(upload_to="images/",default="images/")

    def __str__(self):

        return self.user.username


