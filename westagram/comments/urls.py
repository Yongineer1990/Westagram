from django.urls import path
from .views import Write, Update

urlpatterns = [
    path("", Write.as_view(), name="main"),
    path("update/", Update.as_view())
]
