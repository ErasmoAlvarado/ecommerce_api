from django.urls import path
from .views import DetailBook, DetailCategory, DetailProduct, ListBook, ListCategory, ListProduct

urlpatterns = [
    path('products', ListProduct.as_view()),
    path('products/<str:pk>', DetailProduct.as_view()),
    path('books', ListBook.as_view()),
    path('books/<str:pk>', DetailBook.as_view()),
    path('categorys', ListCategory.as_view()),
    path('categorys/<str:pk>', DetailCategory.as_view())
    
    
    
]
