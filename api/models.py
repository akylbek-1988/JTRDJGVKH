from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Teacher(TimestampedModel):
    name = models.CharField(max_length=160)
    position = models.CharField(max_length=160)
    specialization = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Course(TimestampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name="courses")
    duration = models.CharField(max_length=100, blank=True)
    subjects = models.TextField(blank=True)
    curriculum = models.TextField(blank=True)

    def __str__(self):
        return self.title


class News(TimestampedModel):
    title = models.CharField(max_length=240)
    author = models.CharField(max_length=160)
    category = models.CharField(max_length=100)
    excerpt = models.TextField()
    content = models.TextField()
    published_at = models.DateField()

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title


class Event(TimestampedModel):
    title = models.CharField(max_length=240)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=240)
    description = models.TextField()

    class Meta:
        ordering = ["date", "time"]

    def __str__(self):
        return self.title


class GalleryItem(TimestampedModel):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)


class Book(TimestampedModel):
    title = models.CharField(max_length=240)
    author = models.CharField(max_length=160)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    file_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class FAQ(TimestampedModel):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]


class Application(TimestampedModel):
    full_name = models.CharField(max_length=160)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name="applications")
    message = models.TextField(blank=True)
    status = models.CharField(max_length=30, default="new")

    def __str__(self):
        return self.full_name


class ContactMessage(TimestampedModel):
    name = models.CharField(max_length=160)
    email = models.EmailField()
    subject = models.CharField(max_length=240)
    message = models.TextField()

