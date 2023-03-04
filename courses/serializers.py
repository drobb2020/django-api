from rest_framework import serializers

from .models import Album, Course, Song


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "url", "name", "language", "description", "price")


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        fields = ("id", "album_title", "genre")


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ("id", "song_title", "album")
