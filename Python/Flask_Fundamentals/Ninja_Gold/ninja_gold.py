
from flask import Flask,render_template, request, redirect, session
import random, datetime
app = Flask(__name__)
app.secret_key = 'asdkkajbdlsdjf'

@app.route('/')
def index():
     try:
         session['money'] = session['money']
     except KeyError:
         session['money'] = 0

     try:
         session['log'] += session['log1']
     except KeyError:
         session['log'] = ""
     return render_template('ninja.html')

@app.route('/process', methods=['POST'])
def process():
    session['time'] = '{:(%Y/%m/%d %H:%M)}'.format(datetime.datetime.now())
    if request.form['building'] == 'farm':
        session['location'] = request.form['building']
        session['earned'] = random.randint(10,20)
        session['money'] += session['earned']

    elif request.form['building'] == 'cave':
        session['location'] = request.form['building']
        session['earned'] = random.randint(5,10)
        session['money'] += session['earned']

    elif request.form['building'] == 'house':
        session['location'] = request.form['building']
        session['earned'] = random.randint(2,5)
        session['money'] += session['earned']

    elif request.form['building'] == 'casino':
        session['location'] = request.form['building']
        session['earned'] = random.randint(-50,50)
        session['money'] += session['earned']
        if session['earned'] < 0:
            session['log1'] = '<p style="color:red">You lost '+ str(abs(session['earned'])) + ' golds at the casino...Ouch'+session['time']+'</p>'
            return redirect('/')
        else:
            session['log1'] = '<p style="color:green">You won '+ str(session['earned']) + ' golds at the casino...'+session['time']+'</p>'
            return redirect('/')

    session['log1'] = '<p style="color:green">You earned '+str(session['earned'])+' golds at '+session['location']+' ... '+session['time']+'</p>'

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
   session.pop('money')
   session.pop('log')

   return redirect('/')

app.run(debug=True)
