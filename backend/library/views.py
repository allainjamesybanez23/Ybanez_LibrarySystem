from django.shortcuts import render
<<<<<<< HEAD:backend/backend/backend/library/views.py
from rest_framework import viewsets
=======
<<<<<<< HEAD
from rest_framework import viewsets
=======
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
>>>>>>> dec0a3d8a5ca3284071ba889f30e548eb12d5a7c
>>>>>>> b7a08b98aa31bb42367216a70a867d88a62950e9:backend/library/views.py
from .models import Student, Book, Transaction
from .serializers import StudentSerializer, BookSerializer, TransactionSerializer

# Create your views here.

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer