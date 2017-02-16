from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey/index.html')

def submit(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['text'] = request.POST['text']
        request.session['count'] = request.session['count'] + 1
    return render(request, 'survey/result.html')

def goback(request):
    if request.method == "POST":
        return redirect('/')
