from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views import View
from django.contrib.auth import  authenticate

from  account.models import UserProfile,User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import *
from .forms import ProductCreateForm, ProductImageFrom


class CreateProducts(View):

    def post(self, request):
        form = ProductCreateForm(request.POST)
        images = request.FILES.getlist('images')
        if form.is_valid:
            formdata = form.save()

            for img in images:
                ProductImages.objects.create(product=formdata, image=img)
        else:
            print(form, "is not vaild data ")
        return HttpResponse("data subbmited")

    def get(self, request):
        form = ProductCreateForm
        img_form = ProductImageFrom

        return render(request, 'products/createproduct.html', {'form': form, 'img_form': img_form})


class ProductListView(View):

    def get(self, request):
        context={}

        if request.user.is_authenticated:
            cart_item = Cart.objects.filter(user=request.user)
            # user = UserProfile.objects.get(user=request.user)
            # context['user'] = user

            context['cart_item']=cart_item
        products = Product.objects.all()
        categories = Category.objects.all()
        context['products'] = products
        context['categories'] =categories

        return render(request, 'products/productlist.html', context)


class ProductSearch(View):
    def get(self, request):
        data = {}

        search = request.GET.get('search')
        category = request.GET.get('category')
        if (category != "") and (search != ""):
            print(search)
            print(category)
            products = Product.objects.filter(name__startswith=search, category__name=category)
            data['products'] = products
        elif search != "":
            print("second")
            print(search)
            products = Product.objects.filter(name__startswith=search)
            data['products'] = products
        else:
            print("no data ")

        return render(request, 'products/suggestions.html', data)


class ProductDetail(View):

    def get(self, request, id):
        context = {}
        if request.user.is_authenticated:
            cart_item = Cart.objects.filter(user=request.user)
            context['cart_item'] = cart_item
            # user = UserProfile.objects.get(user=request.user)
            # context['user'] = user

        product = Product.objects.get(id=id)
        context['product_detail'] = product

        print(product.name)
        print(product.category)

        return render(request, 'products/productdetail.html', context)


class AddToCart(View):
    @method_decorator(login_required(login_url='/account/'))
    def get(self, request):
        data = {}
        product_id = request.GET.get('add_product')
        product = Product.objects.get(id=product_id)
        data['product'] = product
        # import  pdb; pdb.set_trace()
        if request.user.is_authenticated:

            obj = Cart.objects.update_or_create(user=request.user, product=product)
            obj.save()

            data['add_to_cart'] = obj

        return render(request, 'products/cart.html', data)


class RemoveFromCart(View):
    def get(self, request):
        data = {}
        product_id = request.GET.get('add_product')
        product = Product.objects.get(id=product_id)
        obj, add_to_cart = Cart.objects.update_or_create(user=request.user)
        obj.save()

        print(obj)
        if product in obj.cart_item.all():
            obj.product.remove(product)
            data['add_to_cart'] = obj

        return render(request, 'products/cart.html', data)
