
from django.urls import path
from . import views

urlpatterns = [
    path("",views.ProductListView.as_view(),name="list_products"),
    path("create/",views.CreateProducts.as_view(),name="create_products"),
    path("search/", views.ProductSearch.as_view(), name="search_products"),

]