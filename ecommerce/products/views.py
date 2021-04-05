from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from .models import Product,ProductImages
from .forms import ProductCreateForm,ProductImageFrom


class CreateProducts(View):

    def post(self,request):
        form=ProductCreateForm(request.POST)
        images = request.FILES.getlist('images')
        if form.is_valid:
            formdata=form.save()

            for img in images:
                ProductImages.objects.create(product=formdata,image=img)
        else:
            print(form,"is not vaild data ")
        return HttpResponse("data subbmited")

    def get(self,request):
        form=ProductCreateForm
        img_form=ProductImageFrom

        return render(request,'products/createproduct.html',{'form':form,'img_form':img_form})

class ProductListView(View):

    def get(self,request):
        products=Product.objects.all()
        return render(request,'products/productlist.html',{'products':products})

    




        