from flask import Blueprint, render_template, session, redirect, url_for
from source.database.database import obtener_conexion 
# Define el blueprint
visualizar_usuarios_bp = Blueprint('visualizar_usuarios_bp', __name__)

# Ruta del blueprint
@visualizar_usuarios_bp.route('/usuarios/admin/visualizar_usuarios')
def visualizar_usuarios():
    if 'rol' not in session or session['rol'] != 1:
        return redirect(url_for('inicio_de_seccion_bp.inicio_de_seccion'))  # Bloquea acceso a usuarios comunes

    conexion = obtener_conexion()
    miCursor = conexion.cursor(dictionary=True)  

    miCursor.execute("SELECT * FROM usuario")
    usuarios = miCursor.fetchall()

    miCursor.close()
    conexion.close()

    return render_template('usuarios/admin/visualizar_usuarios.html', usuarios=usuarios)
