from django.urls import path, include
from .views import register_view, create_contact

urlpatterns = [
    path('contacts/', include('contacts.urls')),  # For contact-related endpoints
    path('users/', include('users.urls')),        # For user-related endpoints
    path('courses/', include('courses.urls')),    # Include course-related URLs
    path('api/register/', register_view, name='api_register_user'),  # API-based registration
    path('api/create-contact/', create_contact, name='create_contact'),  # API to create contact
]
