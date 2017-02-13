from flask import Flask, request, redirect, render_template, flash, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friends')
app.secret_key="1dh63d2;34sHz~!_235hgkmx"

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    abc = mysql.query_db(query)
    return render_template('index.html', all_friends=abc)

@app.route('/friends', methods = ['POST'])
def create():
    print request.form['first_name']
    print request.form['last_name']
    print request.form['email']
    query = "INSERT INTO friends(first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/goto', methods=['GET'])
def goto(id):
    query = "SELECT * FROM friends"
    mysql.query_db(query)
    return render_template('edit.html', id=id)

@app.route('/friends/<id>/edit', methods=['POST'])
def edit(id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, created_at = NOW() WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'id': id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
