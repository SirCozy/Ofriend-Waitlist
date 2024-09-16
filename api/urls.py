from django.urls import path, include

urlpatterns = [
    path('contacts/', include('contacts.urls')),  # Contact-related URLs
]
