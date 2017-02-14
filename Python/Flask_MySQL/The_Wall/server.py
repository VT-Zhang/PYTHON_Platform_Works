from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key="1dh63d2;34sHz~!_235hgkmx"
mysql = MySQLConnector(app, 'the_wall')


@app.route('/', methods=['GET'])
def index():
    # session.pop('_flashes', None)
    return render_template('login.html')

@app.route('/new_user', methods=['GET'])
def goto():
    return render_template('new_user.html')

@app.route('/wall', methods=['GET'])
def load_wall():
    return render_template('wall.html')


@app.route('/login', methods = ['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    query = "SELECT * FROM users WHERE email= :email LIMIT 1"
    data = {'email': email}
    user = mysql.query_db(query, data)
    if user == []:
        session['color'] = 'red'
        flash("Please enter a valid password")
        return redirect('/')
    if bcrypt.check_password_hash(user[0]['password'], password):
        session['color'] = 'green'
        flash("You have successfully logged in!")
        session['id'] = user[0]['id']
        session['first_name'] = user[0]['first_name']
        session['last_name'] = user[0]['first_name']
        return redirect('/wall')
    else:
        session['color'] = 'red'
        flash("The email and password you entered do not match our record!")
        return redirect('/')


@app.route('/register', methods = ['POST'])
def register():

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm'] = request.form['confirm']

    text = '<p>Error(s):</p>'
    text2 = 'Successfully Registered!'
    session['color'] = 'red'
    validation = True

    if len(session['email']) < 1 or len(session['first_name']) < 1 or len(session['last_name']) < 1 or len(session['password']) < 1 or len(session['confirm']) < 1:
        text += '<p>All fields are required and must not be blank.</p>'
        validation = False
    if str.isalpha(str(session['first_name'])) == False or str.isalpha(str(session['last_name'])) == False:
        text += '<p>First and Last Name cannot contain any numbers. </p>'
        validation = False
    if len(session['first_name']) < 2 or len(session['last_name']) < 2:
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
       return redirect('/new_user')

    if validation == True:
       flash(text2)
       session['color'] = 'green'
       pw_hash = bcrypt.generate_password_hash(request.form['password'])
       query = "INSERT INTO users(first_name, last_name, email, password, created_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW())"
       data = {
               'first_name': request.form['first_name'],
               'last_name': request.form['last_name'],
               'email': request.form['email'],
               'pw_hash': pw_hash
              }
       mysql.query_db(query, data)
       return redirect('/wall')

@app.route('/post', methods=['POST'])
def post_message():
    session['message'] = request.form['post_text']
    query = "INSERT INTO messages(users_id, message, created_at) VALUES (:user_id, :message, NOW())"
    data = {
            'user_id': session['id'],
            'message': session['message']
           }
    mysql.query_db(query, data)
    # p = mysql.query_db(query, data)
    # session['time'] = p[0]['created_at']

    return redirect('/wall')

app.run(debug=True)
