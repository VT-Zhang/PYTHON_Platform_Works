from flask import Flask, session, redirect, render_template, request
app = Flask(__name__)
app.secret_key="1dh63d2;34sHz~!_235hgkmx"

@app.route('/')
def index():
    session['no_ninja'] = '<h1>No Ninja here!</h1>'
    return render_template('index.html')

@app.route('/ninja')
def show_all_four_ninjas():
    session['display_off'] = 'display: none;'
    session['display'] = 'display: inline;'
    session['four'] = '<img src="0.png" alt="all_four">'
    return redirect('/')

app.run(debug=True)
