from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from .pagination import MyPagination

# Create your views here.

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPagination
    

