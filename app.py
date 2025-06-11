from flask import Flask, render_template, url_for, request
from source.database.database import obtener_conexion #Importando conexion datebase

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

@app.route('/inicio_de_seccion')
def inicio_de_seccion():
    return render_template('inicio_de_seccion.html')

@app.route('/registrarse', methods = ['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        nombre          = request.form['nombre']
        apellido        = request.form['apellido']
        gmail           = request.form['gmail']
        contrasena      = request.form['contrasena']
        telefono        = request.form['telefono']
        direccion       = request.form['direccion']
        dni             = request.form['dni']
        id_tipo_usuario = 2

        conecion_database = obtener_conexion()
        miCursor = conecion_database.cursor() 

        sql = "INSERT INTO usuario(nombre_cliente, apellido_cliente, email, contrasena, telefono, direccion, dni, id_tipo_usuario) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (nombre, apellido, gmail, contrasena, telefono, direccion, dni, id_tipo_usuario)

        miCursor.execute(sql, valores)
        conecion_database.commit()

        miCursor.close()
        conecion_database.close()
    return render_template('registrarse.html')

if __name__ == '__main__':
    app.run(debug=True)