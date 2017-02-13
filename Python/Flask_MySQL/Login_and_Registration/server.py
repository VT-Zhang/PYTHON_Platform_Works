from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key="1dh63d2;34sHz~!_235hgkmx"
mysql = MySQLConnector(app, 'logindb')

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    session['first'] = request.form['first']
    session['last'] = request.form['last']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm'] = request.form['confirm']

    text = '<p>Error(s):</p>'
    text2 = 'Successfully Registered!'
    session['color'] = 'red'
    validation = True

    if len(session['email']) < 1 or len(session['first']) < 1 or len(session['last']) < 1 or len(session['password']) < 1 or len(session['confirm']) < 1:
        text += '<p>All fields are required and must not be blank.</p>'
        validation = False
    if str.isalpha(str(session['first'])) == False or str.isalpha(str(session['last'])) == False:
        text += '<p>First and Last Name cannot contain any numbers. </p>'
        validation = False
    if len(session['first']) < 2 or len(session['last']) < 2:
        text += '<p>Names should be more than 2 characters. </p>'
        validation = False
    if not EMAIL_REGEX.match(session['email']):
        text += '<p>Invalid email address. </p>'
        validation = False
    if len(session['password']) < 8:
        text += '<p>Password should be more than 8 characters. </p>'
        validation = False
    if session['password'] != session['confirm']:
        text += '<p>Passwords do not match. </p>'
        validation = False

    if validation == False:
       flash(text)
       return redirect('/')
    if validation == True:
       flash(text2)
       session['color'] = 'green'
       return redirect('/create')

@app.route('/create')
def create():
    pw_hash = bcrypt.generate_password_hash(session['password'])
    query = "INSERT INTO users(first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW())"
    data = {
            'first_name': session['first'],
            'last_name': session['last'],
            'email': session['email'],
            'pw_hash': pw_hash
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/login', methods = ['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email= :email LIMIT 1"
    data = {'email': email}
    user = mysql.query_db(query, data)
    if bcrypt.check_password_hash(user[0]['password'], password):
        session['color'] = 'green'
        flash("You have successfully logged in!")
    else:
        session['color'] = 'red'
        flash("The email and password you entered do not match our record!")
    return redirect('/')



app.run(debug=True)
