
from django.urls import path
from . import views

urlpatterns = [
    path("/home/",views.index,name="thanks"),
    path("/create/",views.CreateProducts.as_view(),name="create_products"),


]