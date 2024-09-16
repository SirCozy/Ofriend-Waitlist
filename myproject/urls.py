"""
URL configuration for the myproject application.

Includes:
- Admin routes
- API routes for the contacts app using Django REST Framework
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contacts.views import ContactViewSet

# Router setup for DRF
router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('admin/', admin.site.urls),            # Admin site routes
    path('api/', include(router.urls)),         # API routes for the contacts app
    path('', include('api.urls')),              # Include other API URLs from api/urls.py
]
