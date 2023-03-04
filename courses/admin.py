from django.contrib import admin

from .models import Album, Course, Song

admin.site.register(Course)
admin.site.register(Album)
admin.site.register(Song)
