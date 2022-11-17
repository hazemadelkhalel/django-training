import imp
from importlib.resources import path
from knox import views as knox_views
from .views import LoginView
from django.urls import path
urlpatterns = [
     path('login/', LoginView.as_view(), name='knox_login'),
]