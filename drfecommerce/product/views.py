from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema
from .models import Category, Product, Brand
from .serializers import CategorySerializer, ProductSerializer, BrandSerializer


class CategoryView(viewsets.ViewSet):
    """
    A Simple ViewSet for listing or retrieving all categories.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)


class BrandView(viewsets.ViewSet):
    """
    A Simple ViewSet for listing or retrieving all brands.
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)


class ProductView(viewsets.ViewSet):
    """
    A Simple ViewSet for listing or retrieving all products.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
