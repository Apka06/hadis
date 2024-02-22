from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Favorites(models.Model):
    number = models.IntegerField(unique = True)
    content = models.CharField(max_length = 255)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return str(self.owner) + " 's " + str(self.number)