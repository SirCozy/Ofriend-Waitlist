from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contacts.views import ContactViewSet

# Router setup for DRF
router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('admin/', admin.site.urls),            # Admin site routes
    path('api/', include(router.urls)),         # API routes for the contacts app (DRF ViewSet)
    path('api/', include('api.urls')),          # Include other API URLs from api/urls.py
    path('users/', include('users.urls')),      # Include user URLs
    path('courses/', include('courses.urls')),  # Include courses URLs
]
