from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def dojo():
    return render_template("dojo_survey.html")

@app.route('/result', methods = ['POST'])
def create_user():
    name = request.form['name']
    if len(name) < 1:
        flash("(Name cannot be empty!)")
    location = request.form['location']
    language = request.form['language']
    text = request.form['text']
    if len(text) < 1:
        flash("(Comment cannot be empty!)")
    return render_template("result.html", name=name, location=location, language=language, text=text)

@app.route('/goback', methods = ['POST'])
def goback():
    return redirect('/')

app.run(debug=True)
