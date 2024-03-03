from django.contrib import admin
from .models import Favorites, Profile, Home, Sqlserverconn

admin.site.register(Favorites)
admin.site.register(Profile)
admin.site.register(Home)
admin.site.register(Sqlserverconn)

