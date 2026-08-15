from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (ApplicationViewSet, BookViewSet, ContactMessageViewSet, CourseViewSet,
                    EventViewSet, FAQViewSet, GalleryViewSet, NewsViewSet, TeacherViewSet)

router = DefaultRouter()
router.register("teachers", TeacherViewSet)
router.register("courses", CourseViewSet)
router.register("news", NewsViewSet)
router.register("events", EventViewSet)
router.register("gallery", GalleryViewSet)
router.register("books", BookViewSet)
router.register("faqs", FAQViewSet)
router.register("applications", ApplicationViewSet)
router.register("contact-messages", ContactMessageViewSet)

urlpatterns = [path("", include(router.urls))]

