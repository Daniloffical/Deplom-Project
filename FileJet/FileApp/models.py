from django.db import models
from ProfileApp.models import User
from django.conf import settings

from django.urls import reverse

from django.forms import ModelForm
# Create your models here.






class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class File(models.Model):
    file_path = models.FileField(upload_to='files/%Y/%m/%d', max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, default="Безіменний файл")
    description = models.TextField(default="Опису нема")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    private = models.BooleanField()
    image = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



    def __str__(self):
        return self.name
    
class Chat(models.Model):
    name = models.CharField(max_length=255)

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    

