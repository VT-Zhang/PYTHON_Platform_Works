from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def dojo():
    return render_template("dojo_survey.html")

@app.route('/result', methods = ['POST'])
def create_user():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['text'] = request.form['text']

    if len(session['name']) < 1 or len(session['text']) < 1 or session['location'] == "none" or session['language'] == "none":
        flash("(All fields need to be answered!)")
        return redirect ('/')
    else:
        flash("Thank you for filling out the form!")
        return render_template("result.html")

@app.route('/goback', methods = ['POST'])
def goback():
    session.clear()
    return redirect('/')

app.run(debug=True)
