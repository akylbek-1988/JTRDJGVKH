from rest_framework import mixins, permissions, viewsets
from .models import Application, Book, ContactMessage, Course, Event, FAQ, GalleryItem, News, Teacher
from .serializers import (ApplicationSerializer, BookSerializer, ContactMessageSerializer,
                          CourseSerializer, EventSerializer, FAQSerializer,
                          GalleryItemSerializer, NewsSerializer, TeacherSerializer)


class PublicContentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeacherViewSet(PublicContentViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseViewSet(PublicContentViewSet):
    queryset = Course.objects.select_related("teacher").all()
    serializer_class = CourseSerializer


class NewsViewSet(PublicContentViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class EventViewSet(PublicContentViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class GalleryViewSet(PublicContentViewSet):
    queryset = GalleryItem.objects.all()
    serializer_class = GalleryItemSerializer


class BookViewSet(PublicContentViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class FAQViewSet(PublicContentViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class ApplicationViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Application.objects.select_related("course").all()
    serializer_class = ApplicationSerializer

    def get_permissions(self):
        return [permissions.AllowAny()] if self.action == "create" else [permissions.IsAdminUser()]


class ContactMessageViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def get_permissions(self):
        return [permissions.AllowAny()] if self.action == "create" else [permissions.IsAdminUser()]

