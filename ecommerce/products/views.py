from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.urls import reverse
from django.views import View
from .models import Product,ProductImages,Category
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
        categories=Category.objects.all()

        return render(request,'products/productlist.html',{'products':products,'categories':categories})

class ProductSearch(View):
    def get(self,request):
        data={}
        search=request.GET.get('search')
        category=request.GET.get('category')
        if  (category!= "") and (search != ""):
            print(search)
            print(category)
            products = Product.objects.filter(name__startswith=search,category__name=category)
            data['products'] = products
        elif search != "":
            print("second")
            print(search)
            products = Product.objects.filter(name__startswith=search)
            data['products'] = products
        else:
            print("no data ")


        return render(request,'products/suggestions.html',data)





    




        