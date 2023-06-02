from django.db import models
from ProfileApp.models import User
# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='image/%Y/%m/%d', blank=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name