from django.urls import path
from .views import UserRegisterView, ProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),

]
