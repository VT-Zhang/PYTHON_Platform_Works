from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import abc, User, Course

def index(request):
    context = {
        "users": User.objects.all(),
        "courses": Course.objects.all()
    }
    return render(request, 'testmodels/index.html', context)

def add(request):
    if request.method==['POST']:
        abc.objects.create(user=request.POST['Users'], course=request.POST['Courses'])
        return redirect(reverse('testmodels:index'))
