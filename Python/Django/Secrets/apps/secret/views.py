from django.shortcuts import render, redirect
from django.db.models import Count
from .models import User, Secret, Like
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt


def index(request):
    context = {
        "user": User.objects.all()
    }
    return render(request, 'secret/index.html', context)

def register(request):
    if request.method == 'POST':
        request.session['alert'] = ''
        request.session['alert1'] = 'Registration Success!'
        validation = True

        if len(request.POST['first_name']) < 2 or len(request.POST['last_name']) < 2:
            request.session['alert'] += '<p>Error(s):</p><p>Names cannot be less than 2 letter.</p>'
            validation = False
        if str.isalpha(str(request.POST['first_name'])) == False or str.isalpha(str(request.POST['last_name'])) == False:
            request.session['alert'] += '<p>Names cannot contain any numbers. </p>'
            validation = False
        if len(request.POST['email']) < 1 or len(request.POST['password']) < 1 or len(request.POST['confirm']) < 1:
            request.session['alert'] += '<p>All fields are required and must not be blank.</p>'
            validation = False
        if not EMAIL_REGEX.match(request.POST['email']):
            request.session['alert'] += '<p>Invalid email address.</p>'
            validation = False
        if len(request.POST['password']) < 8:
            request.session['alert'] += '<p>Password should be 8 or more characters.</p>'
            validation = False
        if request.POST['confirm'] != request.POST['password']:
            request.session['alert'] += '<p>Passwords do not match.</p>'
            validation = False

        if validation == False:
            return redirect('/')

        if validation == True:
            hashed = bcrypt.hashpw(request.POST['password'].encode(encoding="utf-8", errors="strict"), bcrypt.gensalt())
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed)
            print user.id
            request.session['id'] = user.id
            request.session['name'] = user.first_name
            request.session['suc'] = 'You have successfully registered.'
            context = {
                "secrets": Secret.objects.all().annotate(counter=Count('secret_like')).order_by('-created_at')[:10]
            }
            return render(request, 'secret/secrets.html', context)


def login(request):
    user = User.objects.filter(email=request.POST['log_email'])
    if bcrypt.checkpw(str(request.POST['log_password']), str(user[0].password)):
        request.session['suc'] = 'You have successfully logged in.'
        request.session['fail'] = ''
        context = {
            "secrets": Secret.objects.all().annotate(counter=Count('secret_like')).order_by('-created_at')[:10]
        }
        return render(request, 'secret/secrets.html', context)
    else:
        request.session['fail'] = 'The email and password you entered do not match! Please try again.'
        return redirect('/')

def create(request):
    Secret.objects.create(post=request.POST['secret'], user_id=request.session['id'])
    context = {
        "secrets": Secret.objects.all().annotate(counter=Count('secret_like')).order_by('-created_at')[:10]
    }
    return render(request, 'secret/secrets.html', context)

def like(request, id):
    Like.objects.create(user_id=request.session['id'], secret_id=id)
    Secret.objects.all().annotate(counter=Count('secret_like'))
    context = {
        "secrets": Secret.objects.all().annotate(counter=Count('secret_like')).order_by('-created_at')[:10]
    }
    return render(request, 'secret/secrets.html', context)

def goto(request):
    context = {
        "secrets": Secret.objects.all().annotate(counter=Count('secret_like')).order_by('-counter')[:10]
    }
    return render(request, 'secret/popular.html', context)

def goback(request):
    context = {
        "secrets": Secret.objects.all().annotate(counter=Count('secret_like')).order_by('-created_at')[:10]
    }
    return render(request, 'secret/secrets.html', context)
