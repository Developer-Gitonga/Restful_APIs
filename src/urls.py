from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('product-list/', views.productList, name="product-list"),
    path('product-detail/<int:id>/', views.productDetail, name="product-detail"),
    path('product-create/', views.productCreate, name="product-create"),
    path('product-delete/<int:id>/', views.productDelete, name="product-delete"),
    path('product-update/<int:id>/', views.productUpdate, name="product-update"),
]