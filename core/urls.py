# backend/core/urls.py
from django.contrib import admin
from django.urls import path, include
from api.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', HomePageView.as_view(), name='home'),
]
