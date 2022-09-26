from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

class Team(models.Model):
    Name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    descri = models.TextField()


    def __str__(self):
        return self.name
    def __str__(self):
       return self.Name