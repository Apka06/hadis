from django.contrib import admin
from .models import FavoritesHadis, FavoritesWord, Home, Sqlserverconn

admin.site.register(FavoritesHadis)
admin.site.register(Home)
admin.site.register(Sqlserverconn)
admin.site.register(FavoritesWord)


