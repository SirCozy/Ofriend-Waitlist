from django.urls import path
from .views import RegisterUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='api_register_user'),
]
