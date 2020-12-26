from django.db import models
from django.utils import timezone
# Create your models here.

class Thought(models.Model):
    thought = models.CharField( max_length=300)
    done = models.BooleanField(default = False)
    #date = models.models.DateField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.thought) + "-  " + str(self.done)




 