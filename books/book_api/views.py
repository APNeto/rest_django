from sys import api_version
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from book_api.models import Book
from book_api.serializer import BookSerializer

# Create your views here.

# def book_list(request):
#     books = Book.objects.all()
#     books_list = list(books.values())
#     return JsonResponse({
#         'books': books_list
#     })
 
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)