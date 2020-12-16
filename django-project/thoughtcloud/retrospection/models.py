from django.db import models

# Create your models here.

class Thought(models.Model):
    thought = models.CharField( max_length=300)
    done = models.BooleanField(default = False)


    def __str__(self):
        return str(self.thought) + "-" + str(self.done)