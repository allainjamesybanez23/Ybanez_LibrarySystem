from rest_framework import serializers
from .models import Student, Book, Transaction

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('student_id', 'name', 'course', 'year')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_id', 'title', 'genre')
        
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('student_id', 'student', 'book', 'date', 'is_returned')