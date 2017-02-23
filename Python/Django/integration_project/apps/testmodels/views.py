from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import abc
from ..course.models import Course
from ..login.models import User

def index(request):
    context = {
        "users": User.objects.all(),
        "courses": Course.objects.all(),
        "register": abc.objects.all()
    }
    return render(request, 'testmodels/index.html', context)

def add(request):
    if request.method== 'POST':
        if adc.objects.isregister(request.POST['user'], request.POST['course']):
            abc.objects.create(user_id=request.POST['users'], course_id=request.POST['courses'])
        else:
            print "User has already registered."
        return redirect(reverse('testmodels:index'))
