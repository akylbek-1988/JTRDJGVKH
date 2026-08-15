from django.contrib import admin
from .models import Application, Book, ContactMessage, Course, Event, FAQ, GalleryItem, News, Teacher

admin.site.register([Teacher, Course, News, Event, GalleryItem, Book, FAQ, Application, ContactMessage])

