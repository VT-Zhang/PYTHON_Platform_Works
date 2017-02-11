from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key="1dh63d2;34sHz~!_235hgkmx"

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def submit():
    session['email'] = request.form['email']
    session['first'] = request.form['first']
    session['last'] = request.form['last']
    session['password'] = request.form['password']
    session['confirm'] = request.form['confirm']

    text = '<p>Error(s):</p>'
    session['color'] = 'red'

    if len(session['email']) < 1 or len(session['first']) < 1 or len(session['last']) < 1 or len(session['password']) < 1 or len(session['confirm']) < 1:
        text += '<p>All fields are required and must not be blank.</p>'

    if str.isalpha(str(session['first'])) == False or str.isalpha(str(session['last'])) == False:
        text += '<p>First and Last Name cannot contain any numbers. </p>'

    if len(session['password']) < 8:
        text += '<p>Password should be more than 8 characters. </p>'

    if not EMAIL_REGEX.match(session['email']):
        text += '<p>Invalid email address. </p>'

    if session['password'] != session['confirm']:
        text += '<p>Passwords do not match. </p>'

    elif text == '':
        flash('Registration Complete!')
        session['color'] = 'green'
        return redirect ('/')

    flash(text)
    return redirect('/')

app.run(debug=True)
