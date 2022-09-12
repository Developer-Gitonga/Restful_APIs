from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('product-list/', views.productList, name="product-list"),
    path('product-detail/<int:id>/', views.productDetail, name="product-detail"),
    path('product-create/', views.productCreate, name="product-create"),
    path('product-delete/<int:id>/', views.productDelete, name="product-delete"),
    path('product-update/<int:id>/', views.productUpdate, name="product-update"),
    path('order-list/', views.orderList, name="order-list"),
    path('order-detail/<int:id>/', views.orderDetail, name="order-detail"),
    path('order-create/', views.orderCreate, name="order-create"),
    path('order-delete/<int:id>/', views.orderDelete, name="order-delete"),
    path('order-update/<int:id>/', views.orderUpdate, name="order-update"),
]