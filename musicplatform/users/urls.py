from django.urls import path
from .views import  UserProfileGenerics
urlpatterns = [
    # path('<int:pk>/',get_user),
    path('<int:pk>/', UserProfileGenerics.as_view()),
]