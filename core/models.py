from django.db import models



class Led(models.Model):
    led = models.IntegerField(default=0)

        