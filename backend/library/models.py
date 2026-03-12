from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    year = models.IntegerField()
    
    def __str__(self):
        return self.student_id + self.name
    
class Book(models.Model):
    book_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
class Transaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    is_Returned = models.BooleanField(default=False)
    
    def __str__(self):
        return self.student.name + " borrowed " + self.book.title