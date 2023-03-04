# from django.shortcuts import render
from rest_framework import viewsets

from .models import Album, Course, Song
from .serializers import AlbumSerializer, CourseSerializer, SongSerializer


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AlbumView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
