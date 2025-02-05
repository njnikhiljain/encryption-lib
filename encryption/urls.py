from django.urls import path
from .views import generate_token_view, verify_token_view

urlpatterns = [
    path('generate/', generate_token_view, name="generate_token"),
    path('verify/', verify_token_view, name="verify_token"),
]
