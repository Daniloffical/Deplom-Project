from django.db import models
from django.contrib.auth.models import User
from SubscriptionApp.models import Subscription

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/%Y/%m/%d', default="unregistered_user.png")
    #in bytes
    total_size = models.IntegerField(default=104857600)
    #in bytes
    used_size = models.IntegerField(default=0)

    procent_size = models.IntegerField(default=0)

    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, to_field='id', default="1")


    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        self.total_size = self.subscription.size
        self.procent_size = int(self.used_size/self.total_size*100)
        
        super(Profile, self).save(*args, **kwargs)