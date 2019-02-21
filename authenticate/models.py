from django.db import models

# Create your models here.

class Register(models.Model):
    fav_color = models.CharField(max_length=100)

    def __str__(self):
        return self.fav_color