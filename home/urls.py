from django.urls import path
from .views import *

app_name = "home"

urlpatterns = [
    path('', welcome_home, name="welcome_home"),
]
