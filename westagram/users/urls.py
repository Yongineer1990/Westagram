from django.urls import path
from .views import SignUp, Login

urlpatterns = [
    path("", SignUp.as_view()),
    path("login/", Login.as_view())
]
