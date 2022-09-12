from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/product-list',
        'Detail View':'/product-detail/<str:pk>',
        'Create':'/product-create',
        'Update':'/product-update/<str:pk>/',
        'Delete':'/product-delete/<str:pk>/',
    }
    return JsonResponse(api_urls) 


@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, id):
    products = Product.objects.get(pk=id)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save
    return Response(serializer.data)


@api_view(['PUT'])
def productUpdate(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['DELETE'])
def productDelete(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        product.delete()
    return Response('Product deleted successfully')