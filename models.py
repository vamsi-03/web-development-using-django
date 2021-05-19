from django.db import models

# Create your models here.
class register(models.Model):
	name = models.CharField(max_length=10)
	email = models.EmailField()
	phone = models.CharField(max_length=10, help_text='enter your mobile number')
