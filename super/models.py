from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_localresident = models.BooleanField(default=False ,null=True)
    is_organiser = models.BooleanField(default=False, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)

class LocalResident(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20, null=True)
    pro_pic = models.ImageField(null=True, blank=True, default="default.jpg")

    def __str__(self):
        return self.user.first_name

class Organiser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20, null=True)
    pro_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name


# the tables for the olympics
class Course(models.Model):
    CHOICES = [("Available", "Available"),
                ("Booked", "Fully Booked")
                ]
    course_name = models.CharField(max_length=80, null=True)
    course_pic = models.ImageField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    cancelled_price = models.FloatField(null=True)
    status = models.CharField(max_length=10, choices=CHOICES)
    price = models.FloatField(null=True)

    class Meta:
        db_table = "Course"


    def __str__(self):
        return self.course_name


class Lecturer(models.Model):
    lecturer_name = models.CharField(max_length=80, null=True)
    lecturer_lastname = models.CharField(max_length=80, null=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    pro_pic = models.ImageField(null=True)

    class Meta:
        db_table = "Lecturer"

    def __str__(self):
        return self.lecturer_name

class Enrollment(models.Model):
    localresident = models.ForeignKey(LocalResident, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    enrol_date = models.DateTimeField(auto_now_add=True, null=True)
    description = models.CharField(max_length=255, null=True)
    lecturer = models.ForeignKey(Lecturer, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.course.course_name

class Article(models.Model):
    title = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(null=True)
    body = models.CharField(max_length=1000 ,null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Article"

class Sport(models.Model):
    sport_name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(null=True)

    def __str__(self):
        return self.sport_name

    class Meta:
        db_table = "Sports"


class Venue(models.Model):
    venue_name = models.CharField(max_length=200, null=True)
    picture = models.ImageField(null=True)
    description = models.CharField(max_length=400, null=True)
    capacity = models.IntegerField(null=True ,blank=True, default=1)

    def __str__(self):
        return self.venue_name

    class Meta:
        db_table = "Venue"


class Event(models.Model):
    CHOICES = [
        ("1", "Upcoming"),
        ("2", "Current"),
        ]
    event_name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(null=True)
    sport = models.ForeignKey("Sport", on_delete = models.DO_NOTHING)
    venue = models.ForeignKey("Venue", on_delete = models.DO_NOTHING)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.event_name

    class Meta:
        db_table = "Events"


class Schedule(models.Model):
    start_date = models.DateTimeField()
    sports = models.ForeignKey("Sport", on_delete = models.DO_NOTHING)
    event = models.ForeignKey("Event",null=True, on_delete=models.CASCADE)
    venue = models.ForeignKey("Venue", null=True, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.sports.sport_name

    class Meta:
        db_table = "Schedule"