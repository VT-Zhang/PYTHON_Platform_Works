from django.shortcuts import render, redirect, HttpResponse
import random
import datetime

def index(request):
    try:
        request.session['money'] = request.session['money']
    except KeyError:
        request.session['money'] = 0
    try:
        request.session['log'] += request.session['log1']
    except KeyError:
        request.session['log'] = ""
    return render(request, "gold/index.html")

def process(request):
    if request.method == "POST":
            request.session['time'] = '{:(%Y/%m/%d %H:%M)}'.format(datetime.datetime.now())
            if request.POST['building'] == 'farm':
                request.session['location'] = request.POST['building']
                request.session['earned'] = random.randint(10,20)
                request.session['money'] += request.session['earned']

            elif request.POST['building'] == 'cave':
                request.session['location'] = request.POST['building']
                request.session['earned'] = random.randint(5,10)
                request.session['money'] += request.session['earned']

            elif request.POST['building'] == 'house':
                request.session['location'] = request.POST['building']
                request.session['earned'] = random.randint(2,5)
                request.session['money'] += request.session['earned']

            elif request.POST['building'] == 'casino':
                request.session['location'] = request.POST['building']
                request.session['earned'] = random.randint(-50,50)
                request.session['money'] += request.session['earned']
                if request.session['earned'] < 0:
                    request.session['log1'] = '<p style="color:red">You lost '+ str(abs(request.session['earned'])) + ' golds at the casino...Ouch'+request.session['time']+'</p>'
                    return redirect('/')
                else:
                    request.session['log1'] = '<p style="color:green">You won '+ str(request.session['earned']) + ' golds at the casino...'+request.session['time']+'</p>'
                    return redirect('/')

            request.session['log1'] = '<p style="color:green">You earned '+str(request.session['earned'])+' golds at '+request.session['location']+' ... '+request.session['time']+'</p>'

            return redirect('/')

def reset(request):
   del request.session['money']
   del request.session['log']
   return redirect('/')
