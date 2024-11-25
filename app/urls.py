from django.urls import path
from .views import LoginViewset

urlpatterns = [
    path("login", LoginViewset.as_view({'post': 'post'}), name="login")
]