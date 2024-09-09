from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .pagination import MyCursorPagination
from .models import Student
# Create your views here.

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyCursorPagination