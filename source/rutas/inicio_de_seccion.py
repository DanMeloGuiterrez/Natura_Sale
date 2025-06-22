from flask import Blueprint, render_template, url_for, request, redirect, flash, session
from source.database.database import obtener_conexion 
from werkzeug.security import check_password_hash  

# Define el blueprint
inicio_de_seccion_bp = Blueprint('inicio_de_seccion_bp', __name__)

# Ruta del blueprint
@inicio_de_seccion_bp.route('/inicio_de_seccion', methods=["POST", "GET"])
def inicio_de_seccion():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["contrasena"]
        
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = '''SELECT id_usuario, nombre_cliente, apellido_cliente, email, contrasena, telefono, direccion, dni, 
                 id_tipo_usuario FROM usuario WHERE email = %s'''
        cursor.execute(sql, (username,))
        fila_email = cursor.fetchone()
        cursor.close()
        conexion.close()
        
        if fila_email: 
            if  check_password_hash(fila_email[4], password):
                # Usuario autenticado correctamente  
                session['rol'] = fila_email[8]
                session['nombre'] = fila_email[1]      # nombre_cliente
                session['apellido'] = fila_email[2]    # apellido_cliente
                session['email'] = fila_email[3]       # email
                session['telefono'] = fila_email[5]    # telefono
                session['direccion'] = fila_email[6]   # direccion
                session['dni'] = fila_email[7]         # dni

                return redirect (url_for('verificar_rol_bp.verificar_rol'))  # o donde desees llevarlo
            else:
                flash("Correo o contraseña incorrecta")
                return render_template ('usuarios/inicio_de_seccion.html')
        else: 
            flash ("Usuario no registrado.")
            return render_template ('usuarios/inicio_de_seccion.html')
    else:
        return render_template('usuarios/inicio_de_seccion.html')