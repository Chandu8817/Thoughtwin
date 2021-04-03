from django.db import models
from django.contrib.auth.models import User
CATEGORY=(
    ('MOB','mobile'),
    ('CL','Cloths'),
    ('EL','Electronics'),
    ('SP','Sports'),
    ('HOAP','Home Applications'),

)

class Product(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY,max_length=100)
    description=models.TextField(max_length=100)
    image=models.FileField(upload_to='images/productimages/',default='images/productimages/dummy.png',blank=True)
    price=models.IntegerField(default=0)
    rating=models.ManyToManyField(User,blank=True,related_name='rating')
    

    def __str__(self):
        return self.name

    @property
    def rating_count(self):
        return self.rating.count()



