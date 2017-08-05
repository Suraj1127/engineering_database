from django.db import models
from django.utils import timezone

# Create your models here.
class Record(models.Model):
	name = models.CharField(max_length=15)
	qualification = models.CharField(max_length=20)
	years = models.BigIntegerField()
	district = models.CharField(max_length=15)
	data_number = models.BigIntegerField()

	def __str__(self):
		return self.name