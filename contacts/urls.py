from django.urls import path
from .views import ContactListCreate

urlpatterns = [
    path('contact/', ContactListCreate.as_view(), name='contact-list-create'),
]
# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contacts.views import ContactViewSet, home  # Import the home view

# Router setup for DRF
router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the API routes from the router
    path('', home, name='home'),  # Map the root URL to the home view
]
