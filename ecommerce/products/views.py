from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from .models import Product
from .forms import ProductCreateForm

def index(request):
    return HttpResponse("home")


class CreateProducts(View):



    def get(self,request):

        form=ProductCreateForm
        