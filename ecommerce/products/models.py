from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, related_name='category')
    description = models.TextField(max_length=1000)
    price = models.IntegerField(default=0)
    rating = models.ManyToManyField(User, blank=True, related_name='rating')

    def __str__(self):
        return self.name

    def get_image_filename(instance, filename):
        name = name.product.title
        slug = slugify(name)
        return "images/productimages/%s-%s" % (slug, filename)

    @property
    def rating_count(self):
        return (self.rating.count())

    @property
    def sorted_image_set(self):
        return self.product_images.order_by('time_created')


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.FileField(upload_to='images/productimages/',
                             default='images/productimages/dummy.png', blank=True)
    time_created = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.product.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,blank=True,null=True)
