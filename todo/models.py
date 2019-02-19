from django.db import models

# Create your models here.

class sample(models.Model):
	name = models.CharField(max_length=30)
	password = models.BooleanField(default=False)

	def __str__(self):
		return self.name
