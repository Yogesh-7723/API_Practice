from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework import status
import json
from rest_framework.response import Response
from .models import *
# from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
def get_quiz(request):
    try:
        question_objs = Question.objects.all()
        data = []
        for question_obj in question_objs:
            data.append({
                'category': question_obj.category,
                'question': question_obj.question,
                'marks': question_obj.marks
            })
            data = json.loads(data)
        return JsonResponse({'data': data}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)