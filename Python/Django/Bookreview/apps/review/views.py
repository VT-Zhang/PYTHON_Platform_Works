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
        preuser = User.objects.filter(email=request.POST['email'])
        if preuser:
            request.session['alert'] = 'The user already exists, please try another email.'
            return redirect('/')

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
            request.session['email'] = request.POST['email']
            request.session['user_id'] = user.id
            request.session['name'] = user.name
            request.session['alias'] = user.alias
            context = {
                "user": User.objects.get(email=request.POST['email']),
                "books": Book.objects.all().order_by('-created_at')[:5],
                "reviews": Review.objects.all().order_by('-created_at')[:5],
                "boobs": Book.objects.all().order_by('title')
            }
            return render(request, 'review/main.html', context)


def login(request):
    user = User.objects.filter(email=request.POST['log_email'])
    if not user:
        request.session['fail'] = "The email you entered does not exist, please register!"
        return redirect('/')

    if bcrypt.checkpw(str(request.POST['log_password']), str(user[0].password)):
        request.session['fail'] = ''
        context = {
            "user": User.objects.get(email=request.POST['log_email']),
            "books": Book.objects.all().order_by('-created_at')[:5],
            "reviews": Review.objects.all().order_by('-created_at')[:5],
            "boobs": Book.objects.all().order_by('title')
        }
        request.session['user_id'] = user[0].id
        request.session['name'] = user[0].name
        request.session['alias'] = user[0].alias
        request.session['email'] = request.POST['log_email']
        return render(request, 'review/main.html', context)

    else:
        request.session['fail'] = 'The email and password you entered do not match! Please try again.'
        return redirect('/')


def main(request):
    user = User.objects.filter(email=request.session['email'] )
    print request.session['user_id']

    context = {
        "books": Book.objects.all().order_by('-created_at')[:5],
        "reviews": Review.objects.all().order_by('-created_at')[:5],
        "boobs": Book.objects.all().order_by('title')
    }
    return render(request, 'review/main.html', context)


def goto(request):
    return render(request, 'review/review.html')


def create(request):
    if request.method == 'POST':
        book = Book.objects.create(title=request.POST['title'], author=request.POST['author'])
        request.session['book_id'] = book.id
        Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], user_id=request.session.get('user_id'), book_id=request.session['book_id'])
        context = {
            "books": Book.objects.all().order_by('-created_at')[:5],
            "reviews": Review.objects.all().order_by('-created_at')[:5],
            "boobs": Book.objects.all().order_by('title')
        }
        return render(request, 'review/main.html', context)


def book(request, id):
    context = {
        "book": Book.objects.get(id=id),
        "reviews": Review.objects.filter(book_id=id).order_by('-created_at')
    }
    return render(request, 'review/book.html', context)

def add(request, id):
    if request.method == 'POST':
        context = {
            "book": Book.objects.get(id=id),
            "reviews": Review.objects.filter(book_id=id).order_by('-created_at')
        }
        Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], user_id=request.session['user_id'], book_id=id)
        return render(request, 'review/book.html', context)

def user(request, id):
    counter = Review.objects.filter(user_id=id).count()
    context = {
        "user": User.objects.get(id=id),
        "reviews": Review.objects.filter(user_id=id).order_by('-created_at'),
        "counter": counter
    }
    return render(request, 'review/user.html', context)

def logout(request):
    request.session.pop('user_id')
    request.session.pop('name')
    request.session.pop('alias')
    request.session.pop('email')
    return redirect('/')
