from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Hadis_Deryasi.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',include('accounts.urls')),
]
