from django.shortcuts import render, redirect
from .models import Course

def index(request):
    context = {
    "courses":Course.objects.all()
    }
    return render(request, "cou/index.html", context)

def add(request):
    if request.method=="POST":
        Course.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
        return redirect('/')

def next(request, id):
    context = {"id": id}
    # delcou = Course.objects.get(id=id)
    return render(request, "cou/delete.html",context)

def delete(request, id):
    if request.method=="POST":
        Course.objects.filter(id=id).delete()
        return redirect('/')

def goback(request):
    if request.method=="POST":
        return redirect('/')
