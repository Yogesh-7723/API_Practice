from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerialize
# Create your views here.

# class MyThrottle(AnonRateThrottle):
#     scope = 'jack'

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialize
    authentication_classes = [SessionAuthentication]
    # throttle_classes = [UserRateThrottle,MyThrottle]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'




