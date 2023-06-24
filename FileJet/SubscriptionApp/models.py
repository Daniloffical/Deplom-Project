from django.db import models

# Create your models here.

class Subscription(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='image/%Y/%m/%d')
    price = models.IntegerField(default=0)
    size = models.IntegerField(default=0)

    def __str__(self):
        return self.name