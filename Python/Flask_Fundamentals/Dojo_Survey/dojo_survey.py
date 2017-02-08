from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def dojo():
    return render_template("dojo_survey.html")

@app.route('/result', methods = ['POST'])
def create_user():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    text = request.form['text']
    return render_template("result.html", name=name, location=location, language=language, text=text)

@app.route('/goback', methods = ['POST'])
def goback():
    return redirect('/')

app.run(debug=True)
