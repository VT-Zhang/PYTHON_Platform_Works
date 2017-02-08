from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def sumSessionCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

@app.route('/')
def index():
    sumSessionCounter()
    return render_template("counter.html")

@app.route('/plus2', methods = ['POST'])
def plus2():
    session['counter'] += 2
    return render_template("counter.html")

@app.route('/clear', methods = ['POST'])
def clearSession():
    session['counter'] = 0
    return render_template("counter.html")

app.run(debug=True)
