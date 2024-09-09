from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SingerSerializer,SongSerializer
from .pagination import MyCursorPagination
from .models import Singer,Song
# Create your views here.

class SingerView(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
