from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import viewsets
# Create your views here.

# searching functionality of filter
# class StudentView(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['city']
    # search_fields = ['$city']
    # search_fields = ['city','name']
    # search_fields = ['^city'] # if match fstart with
    # search_fields = ['=city','=name'] # return only fully matched

# ordering functionality of api
class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name','city','id','roll']