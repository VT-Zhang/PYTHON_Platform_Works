from flask import Flask,render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['num'] = random.randrange(0,100)
    return render_template("index.html")

@app.route('/guess', methods = ['POST'])
def guessGame():
    session['guessNum'] = request.form['guessNum']
    try:
        if int(session['guessNum']) > session['num'] :
            word = "Too High!"
            color = "red"
            return render_template("index.html", word=word, color=color)

        elif int(session['guessNum']) < session['num'] :
            word = "Too Low!"
            color = "yellow"
            return render_template("index.html", word=word, color=color)

        elif int(session['guessNum']) == session['num'] :
            word = "Congrats! " + session['guessNum'] + " was the number!"
            color = "green"
            return render_template("index.html", word=word, color=color, display="display: inline;")

    except ValueError:
        return redirect('/')


@app.route('/reset', methods=['POST'])
def reset():
    return redirect('/')

app.run(debug=True)
