from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Home(models.Model):
    def __str__(self) -> str:
        return "home"

class FavoritesHadis(models.Model):
    number = models.IntegerField(null = True)
    content = models.CharField(max_length = 255)
    book = models.CharField(max_length = 255, null=True)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)

    def arrange_text(self):
        text = str(self.number) + " - " + str(self.content) + "\n-" + str(self.book) + "-\n"
        return text

    def __str__(self) -> str:
        return str(self.owner) + " 's " + str(self.id)
    
class FavoritesWord(models.Model):
    number = models.IntegerField(null = True)
    word = models.CharField(max_length = 255)
    meaning = models.CharField(null = True, max_length = 512)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def arrange_text(self):
        text = str(self.number) + "\n" + str(self.word) + " : " + str(self.meaning) + "\n"
        return text

    def __str__(self) -> str:
        return str(self.owner) + " 's " + str(self.id)
    

class Sqlserverconn(models.Model):

    kid = models.IntegerField(null = True)
    onay = models.BooleanField()
    diger = models.CharField(max_length = 100, null = True)
    isim = models.CharField(max_length = 256, null = True)
    diger2 = models.CharField(max_length = 100, null = True)
    koku = models.CharField(max_length = 100, null = True)
    kelime = models.CharField(max_length = 100, null = True)