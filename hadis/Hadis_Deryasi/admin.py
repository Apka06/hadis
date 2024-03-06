from django.contrib import admin
from .models import FavoritesHadis, Profile, Home, Sqlserverconn

admin.site.register(FavoritesHadis)
admin.site.register(Profile)
admin.site.register(Home)
admin.site.register(Sqlserverconn)

