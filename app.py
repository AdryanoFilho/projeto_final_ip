from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ola():
    # return '<h1>Olá, Mundo!</h1>'
    return render_template('index.html')

@app.route('/sobre_equipe')
def sobre_equipe():
    return render_template('sobre_equipe.html')

app.run()