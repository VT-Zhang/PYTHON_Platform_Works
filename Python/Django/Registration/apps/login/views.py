from django.shortcuts import render
import re
from .models import User
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request, 'login/index.html')

def success(request):
    return render(request, 'login/success.html')
