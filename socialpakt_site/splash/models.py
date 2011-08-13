from django.db import models
from django.forms import ModelForm

# Create your models here.

class Signup(models.Model):
	"""Simple model to record signups"""
	email = models.EmailField()
	def __str__(self):
		return str(self.email)

class SignupForm(ModelForm):
    class Meta:
		model = Signup