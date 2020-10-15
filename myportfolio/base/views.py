from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactForm


# Create your views here.
def home(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    subject = request.GET.get('subject')
    message = request.GET.get('message')

    data = ContactForm(name=name, email=email, subject=subject, message=message)
    data.save()
    return render(request, 'base/index.html', {})

