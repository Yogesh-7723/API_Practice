from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import StudentSerialize


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialize
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)
    




