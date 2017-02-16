from django.shortcuts import render, redirect
import string
import random

def index(request):
    return render(request, 'generator/index.html')


def submit(request):
    if request.method == "POST":
        request.session['counter'] += 1
        request.session['word'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
    return redirect ('/')
