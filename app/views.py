from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.filters import SearchFilter,OrderingFilter

from app.serializers import BookSerializer, CategorySerializer, ProductSerializer
from . import models
from .models import Book, Categorys, Product

class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = ['name', 'price']

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = '__all__'

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListCategory(generics.ListCreateAPIView):
    queryset = Categorys.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter,OrderingFilter)
    search_fields = '__all__'

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorys.objects.all()
    serializer_class = CategorySerializer


   