from flask import Blueprint, render_template, request, redirect, url_for, session
from source.database.database import obtener_conexion 
from werkzeug.security import generate_password_hash  

registrarse_bp = Blueprint('registrarse_bp', __name__)

@registrarse_bp.route('/registrarse', methods=['GET', 'POST'])
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

        # Cifrar la contraseña antes de guardar
        contrasena_hash = generate_password_hash(contrasena)

        conecion_database = obtener_conexion()
        miCursor = conecion_database.cursor() 

        sql = """INSERT INTO usuario(nombre_cliente, apellido_cliente, email, contrasena, telefono, direccion, dni, id_tipo_usuario) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (nombre, apellido, gmail, contrasena_hash, telefono, direccion, dni, id_tipo_usuario)

        miCursor.execute(sql, valores)
        conecion_database.commit()
        miCursor.close()
        conecion_database.close()

        # Guardar datos del usuario en sesión
        session['nombre'] = nombre
        session['apellido'] = apellido
        session['email'] = gmail
        session['telefono'] = telefono
        session['direccion'] = direccion
        session['dni'] = dni
        session['rol'] = id_tipo_usuario

        return redirect(url_for('mostrar_panel_usuario_bp.mostrar_panel_usuario'))
    
    return render_template('usuarios/registrarse.html')
