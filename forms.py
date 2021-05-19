from django import forms
from .models import *

class registrationForm(forms.ModelForm):
	class Meta:
		model = register
		fields = '__all__'

		widgets = {
		'name':forms.TextInput(attrs = {'class':'form-control'}),
		'email':forms.EmailInput(attrs = {'class':'form-control'}),
		'phone':forms.TextInput(attrs = {'class':'form-control'})
		}