from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('product-list/', views.productList, name="product-list"),
    path('product-detail/<str:pk>/', views.productDetail, name="product-detail"),

]