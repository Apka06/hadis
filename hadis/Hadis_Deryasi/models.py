from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class HadisDeryasi(models.Model):
    def __str__(self) -> str:
        return "hadis"

class Home(models.Model):
    def __str__(self) -> str:
        return "home"

class FavoritesHadis(models.Model):
    number = models.IntegerField(unique = True)
    content = models.CharField(max_length = 255)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return str(self.owner) + " 's " + str(self.number)
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return str(self.user)
    
class Sqlserverconn(models.Model):

    onay = models.BooleanField()
    diger = models.CharField(max_length = 100, null = True)
    isim = models.CharField(max_length = 256, null = True)
    diger2 = models.CharField(max_length = 100, null = True)
    koku = models.CharField(max_length = 100, null = True)
    kelime = models.CharField(max_length = 100, null = True)