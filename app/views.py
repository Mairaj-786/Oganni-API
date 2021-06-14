from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin
from .models import Product
from .serializers import ProductSerializer
from rest_framework import filters
# Create your views here.


class ProductView(ListAPIView, ListModelMixin, CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category']
