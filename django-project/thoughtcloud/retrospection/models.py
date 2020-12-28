from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User

class Thought(models.Model):
    thought = models.CharField( max_length=300)
    done = models.BooleanField(default = False)
    #date = models.models.DateField()
    #date = models.DateTimeField(default=timezone.now)
    date = models.DateTimeField(auto_now = True)
    manager = models.ForeignKey(User, on_delete =models.CASCADE, default = None)

    def __str__(self):
        return str(self.thought) + "-  " + str(self.done)

class Time(models.Model):
    time = models.CharField(max_length=20)




 