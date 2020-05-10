from django.db import models

class Address(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	phone = models.CharField(max_length=15)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	province = models.CharField(max_length=200)
	zipcode = models.CharField(max_length=200)

	def __str__(self):
		return self.name
