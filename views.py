from django.shortcuts import render
from .forms import registrationForm
from django.http import HttpResponse
from django.core.mail import send_mail
from Mailsending import settings
from django.core.mail import EmailMessage
from django import forms


def register(request):
	form = registrationForm()
	if request.method == 'POST':
		form = registrationForm(request.POST)
		form.save()
		sub = "success"
		body = "hello ! your registartion is successful"
		from_id = settings.EMAIL_HOST_USER
		to_id = form.cleaned_data['email']
		mail = EmailMessage(sub,body,from_id,[to_id])
		attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
		mail.send()
		return HttpResponse("registration successful")
	return render(request,"request.html",{'form':form}) 