from datetime import datetime
from django.shortcuts import render
from django.utils.translation import deactivate_all
from .models import Book, Category, SubCategory
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import BookSerializer,CategorySerializer,SubCategorySerializer

# Create your views here.

@api_view(['GET'])
def allBooks(request):

    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)
    
@api_view(['GET'])
def activeBooks(request):

    if request.method == 'GET':
        activeBooks = Book.objects.filter(isActive = True)
        serializer = BookSerializer(activeBooks, many = True)
        return Response(serializer.data)

@api_view(['GET'])
def delistedBooks(request):

    if request.method == 'GET':
        delistedBooks = Book.objects.filter(isActive = False)
        serializer = BookSerializer(activeBooks, many = True)
        return Response(serializer.data)

@api_view(['POST'])
def addBook(request):

    if request.method == 'POST':
        if request.user.is_authenticated:
            request.data['addedBy'] = request.user.username
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getBook(request, id):
    try:
        book = Book.objects.get(id = id)
    except Book.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

@api_view(['PUT'])
def editBook(request, id):
    try:
        book = Book.objects.get(id = id)
        book.lastModifiedOn = datetime.now()
        if request.user.is_authenticated:
            book.lastModifiedBy = request.user.username
        book.save()
    except Book.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BookSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteBook(request, id):
    try:
        book = Book.objects.get(id = id)
    except Book.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        book.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def allCategories(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data)

@api_view(['GET'])
def allSubCategories(request):

    if request.method == 'GET':
        subCategories = SubCategory.objects.all()
        serializer = SubCategorySerializer(subCategories, many = True)
        return Response(serializer.data)

@api_view(['POST'])
def addCategory(request):

    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addSubCategory(request):

    if request.method == 'POST':
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def delistBook(request, id):
    try:
        book = Book.objects.get(id = id)
        book.lastModifiedOn = datetime.now()
        if request.user.is_authenticated:
            book.lastModifiedBy = request.user.username
        book.save()
    except Book.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        book.isActive = False
        book.save()
        return Response(status = status.HTTP_200_OK)

