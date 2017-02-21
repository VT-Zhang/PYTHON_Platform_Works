from django.shortcuts import render, redirect
import re
import bcrypt
from .models import User
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    context = {
    "users":User.objects.all()
    }
    return render(request, 'login/index.html', context)

def register(request):
    if request.method == 'POST':
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']
        request.session['confirm'] = request.POST['confirm']

        request.session['alert'] = ''
        request.session['alert1'] = 'Registration Success!'
        validation = True

        if len(request.session['first_name']) < 2 or len(request.session['last_name']) < 2:
            request.session['alert'] += '<p>Error(s):</p><p>Names cannot be less than 2 letter.</p>'
            validation = False
        if str.isalpha(str(request.session['first_name'])) == False or str.isalpha(str(request.session['last_name'])) == False:
            request.session['alert'] += '<p>Names cannot contain any numbers. </p>'
            validation = False
        if len(request.session['email']) < 1 or len(request.session['password']) < 1 or len(request.session['confirm']) < 1:
            request.session['alert'] += '<p>All fields are required and must not be blank.</p>'
            validation = False
        if not EMAIL_REGEX.match(request.session['email']):
            request.session['alert'] += '<p>Invalid email address.</p>'
            validation = False
        if len(request.session['password']) < 8:
            request.session['alert'] += '<p>Password should be 8 or more characters.</p>'
            validation = False
        if request.session['confirm'] != request.session['password']:
            request.session['alert'] += '<p>Passwords do not match.</p>'
            validation = False

        if validation == False:
            return redirect('/')
        if validation == True:
            hashed = bcrypt.hashpw(request.session['password'].encode(encoding="utf-8", errors="strict"), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed)
            request.session['name'] = request.POST['first_name']
            request.session['suc'] = 'You have successfully registered.'
            return render(request, 'login/success.html')


def login(request):
    user = User.objects.filter(email=request.POST['log_email'])
    if bcrypt.checkpw(request.POST['log_password'], user[0]['password']) == True:
    # if bcrypt.hashpw(request.POST['log_password'], user[0]['password']) == user[0]['password']:
        request.session['suc'] = 'You have successfully logged in.'
        request.session['fail'] = ''
        return render(request, 'login/success.html')
    else:
        request.session['fail'] = 'The email and password you entered do not match!'
        return redirect('/')
