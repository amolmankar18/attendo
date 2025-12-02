# backend/api/urls.py
from django.urls import path
from .views import HomePageView, IndexView, StudentsMongoView, TeachersMongoView

urlpatterns = [
    path('', IndexView.as_view(), name='api-index'),   # /api/
    path('mongo/students/', StudentsMongoView.as_view(), name='mongo-students'),
    path('mongo/teachers/', TeachersMongoView.as_view(), name='mongo-teachers'),
]
