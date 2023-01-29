from django.db import models

# Create your models here.
class Fruits(models.Model):
	name = models.CharField(max_length=257)
	calories = models.FloatField()

	def __str__(self):
		return self.name 