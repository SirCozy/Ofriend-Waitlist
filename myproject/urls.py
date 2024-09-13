"""
This module defines the URL patterns for the myproject application.

It includes:
- Admin site routes
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
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the API routes from the router
]
