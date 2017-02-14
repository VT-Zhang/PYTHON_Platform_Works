from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('user.html', username=username)

@app.route('/route/with/<vararg>')
def handler_function(vararg):

    print vararg

app.run(debug=True)
