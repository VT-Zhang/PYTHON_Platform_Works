from django.shortcuts import render, redirect
from django.db.models import Count
from .models import User, Book, Review
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import bcrypt

def index(request):
    return render(request, 'review/index.html')

def register(request):
    if request.method == 'POST':
        request.session['alert'] = ''
        validation = True

        if len(request.POST['name']) < 2 or len(request.POST['alias']) < 2:
            request.session['alert'] += '<p>Error(s):</p><p>Names cannot be less than 2 letter.</p>'
            validation = False
        if str.isalpha(str(request.POST['name'])) == False or str.isalpha(str(request.POST['alias'])) == False:
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
            user = User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=hashed)
            print user.id
            request.session['id'] = user.id
            request.session['name'] = user.name
            context = {
                "books": Book.objects.all().order_by('-created_at')[:3]
            }
            return render(request, 'review/main.html', context)


def login(request):
    user = User.objects.filter(email=request.POST['log_email'])
    if bcrypt.checkpw(str(request.POST['log_password']), str(user[0].password)):
        request.session['fail'] = ''
        context = {
            "books": Book.objects.all().order_by('-created_at')[:3]
        }
        return render(request, 'review/main.html', context)
    else:
        request.session['fail'] = 'The email and password you entered do not match! Please try again.'
        return redirect('/')

def goto(request):
    return render(request, 'review/review.html')

def create(request):
    if request.method == 'POST':
        Book.objects.create(title=request.POST['title'], author=request.POST['author'], review=request.POST['review'], rating=request.POST['rating'])
        context = {
            "books": Book.objects.all().order_by('-created_at')[:3]
        }
        return render(request, 'review/main.html', context)

def main(request):
    context = {
        "books": Book.objects.all().order_by('-created_at')[:3]
    }
    return render(request, 'review/main.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def book(request, id):
    context = {
        "book": Book.objects.get(id=id)
    }
    return render(request, 'review/book.html', context)

def add(request, id):
    if request.method == 'POST':
        context = {
            "book": Book.objects.get(id=id)
        }
        return render(request, 'review/book.html', context)

def user(request, id):
    if request.method == 'POST':
        context = {
            "user": User.objects.get(id=id)
        }
        return render(request, 'review/user.html', context)
