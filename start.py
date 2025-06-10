from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/contactanos')
def contactanos():
    return render_template('contactanos.html')

@app.route('/inicio_de_seccion_o_registrarse')
def inicio_de_seccion_o_registrarse():
    return render_template('inicio_de_seccion_o_registrarse.html')

