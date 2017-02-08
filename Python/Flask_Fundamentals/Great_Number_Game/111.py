from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hotdoggy'

#No congratulations

@app.route('/')
def index():
   # import random
   # session['mynumber'] = 55
   # session['mynumber'] = random.randint(1,100)
   return render_template("great_number_game_onepage.html")

@app.route('/checkguess', methods=['POST'])
def checking():
   mynumber = 55
   guess = request.form['guess']

   if int(guess) < mynumber:
       remark = "Too low!"
       color = "red"
       correct = False

   elif int(guess) > mynumber:
       remark = "Too high!"
       color = "red"
       correct = False

   elif int(guess) == mynumber:
       remark = str(mynumber) + " was the number!"
       color = "green"
       correct = True

   return render_template("great_number_game_onepage.html", remark=remark, color=color, correct=correct)

# @app.route('/congratulations')
# def congratulations():
#     remark = "55 was the number!"
#     color = "green"
#     return render_template("congratulations.html", remark=remark, color=color)
#
# @app.route('/goback', methods=['POST'])
# def goback():
#     # session.pop('mynumber')
#     return redirect('/')
