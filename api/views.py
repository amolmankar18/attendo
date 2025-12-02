# backend/api/views.py
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

# Import mongo client lazily to avoid import-time failures if env missing
try:
    from .mongo_client import db
except Exception:
    db = None

# HTML home for '/'
class HomePageView(TemplateView):
    template_name = "index.html"

# JSON index for '/api/'
class IndexView(APIView):
    def get(self, request):
        return Response({
            "message": "Attendo backend running",
            "endpoints": {
                "admin": "/admin/",
                "students_mongo": "/api/mongo/students/",
                "teachers_mongo": "/api/mongo/teachers/"
            }
        })

# Mongo-backed views (they return [] if db not configured)
class StudentsMongoView(APIView):
    def get(self, request):
        if db is None:
            return Response([])
        students = list(db.students.find({}, {"_id": 0}))
        return Response(students)

class TeachersMongoView(APIView):
    def get(self, request):
        if db is None:
            return Response([])
        teachers = list(db.teachers.find({}, {"_id": 0}))
        return Response(teachers)
