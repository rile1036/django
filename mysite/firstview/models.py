from django.db import models

# Create your models here.
class People(models.Model):
	number = models.IntegerField(default=0)
	name = models.CharField(max_length=10)
	intro = models.TextField()
	def __str__(self):
		return self.name
class User(models.Model):
	userID = models.CharField(max_length=200)
	userPassword = models.CharField(max_length=200)
	def __str__(self):
		return self.userID
