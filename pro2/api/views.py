from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_class = TokenAuthentication
    # permission_classes = [IsAuthenticated]