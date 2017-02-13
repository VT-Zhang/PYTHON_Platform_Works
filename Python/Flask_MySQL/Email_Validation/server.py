from flask import Flask, session, render_template, redirect, request, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app, 'email_db')
app.secret_key="1dh63d2;34sHz~!_235hgkmx"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods = ['POST'])
def validate():
    session['email'] = request.form['email']
    if EMAIL_REGEX.match(session['email']):
        flash("The email address you entered '" + session['email'] + "' is a valid address. Thank you!")

        query1 = "INSERT INTO email(email_address, created_at, updated_at) VALUES (:email_address, NOW(), NOW())"
        data = {
                    'email_address': request.form['email']
                }
        mysql.query_db(query1, data)
        query2 = "SELECT * FROM email"
        result = mysql.query_db(query2)
        return render_template('result.html', result=result)

    if not EMAIL_REGEX.match(session['email']):
        flash("Please enter an valid email address!!")
        session['display'] = "display: inline;"
        return redirect('/')

# @app.route('/success', methods = ['POST'])
# def create():
#     query1 = "INSERT INTO email(email_address, created_at, updated_at) VALUES (:email_address, NOW(), NOW())"
#     data = {
#                 'email_address': request.form['email']
#             }
#
#     mysql.query_db(query1, data)
#
#     query2 = "SELECT * FROM email"
#     session['result'] = mysql.query_db(query2)
#
#     return render_template('result.html')

app.run(debug=True)
