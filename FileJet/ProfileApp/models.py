from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='image/%Y/%m/%d', blank=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name