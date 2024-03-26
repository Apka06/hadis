from django.urls import path
from .views import UserRegisterView, ProfileView, FavoritePrintView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('favorites_document/<str:favori>/', FavoritePrintView.as_view(), name='favorites_document'),
]
