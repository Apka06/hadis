from django.urls import path
from .views import HomeView, SqlServerConnView, HadisDeryasiView, SerhView
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('lugat/', SqlServerConnView.as_view(), name="lugat"),
    path('hadis_deryasi/', HadisDeryasiView.as_view(), name="hadis_deryasi"),
    path('serh/', SerhView.as_view(), name="serh")
]
