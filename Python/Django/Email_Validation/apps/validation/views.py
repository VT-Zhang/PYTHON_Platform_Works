from django.shortcuts import render, redirect
import re
from .models import Email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    request.session['color'] = ''
    return render(request, 'validation/index.html')

def submit(request):
    if request.method == "POST":
        request.session['alert'] = ''
        if not EMAIL_REGEX.match(request.POST['email']):
            request.session['alert'] = 'The email you entered is not a valid email format!'
            request.session['color'] = 'background-color: red;'
            return redirect('/')
        else:
            Email.objects.create(address=request.POST['email'])
            context = {
            "emails":Email.objects.all()
            }
            request.session['em'] = request.POST['email']
            request.session['display'] = 'display: flex;'
            return render(request, 'validation/result.html', context)

def goback(request):
    if request.method == "POST":
        return redirect('/')

def delete(request, id):
        Email.objects.filter(id=id).delete()
        context = {
        "emails":Email.objects.all()
        }
        request.session['display'] = 'display: none;'
        return render(request, 'validation/result.html', context)
