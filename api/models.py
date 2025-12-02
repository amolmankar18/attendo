# backend/api/models.py
from django.db import models
from django.utils import timezone

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # store hashed
    department = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    roll_no = models.CharField(max_length=50)
    class_name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ClassSession(models.Model):
    session_id = models.CharField(max_length=40, unique=True)
    subject_name = models.CharField(max_length=200)
    start_ts = models.DateTimeField()
    end_ts = models.DateTimeField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    radius = models.IntegerField(default=50)  # meters
    teacher_id = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Attendance(models.Model):
    attendance_id = models.CharField(max_length=40, unique=True)
    student_id = models.CharField(max_length=20)
    session_id = models.CharField(max_length=40)
    teacher_id = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, default="Present")
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    distance = models.IntegerField(null=True, blank=True)
