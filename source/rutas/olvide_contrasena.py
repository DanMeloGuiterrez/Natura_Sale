from flask import Blueprint, render_template, request, redirect, flash, session, url_for
from source.database.database import obtener_conexion
from werkzeug.security import generate_password_hash

olvide_contrasena_bp = Blueprint('olvide_contrasena_bp', __name__)

@olvide_contrasena_bp.route('/olvide_contrasena', methods=["GET", "POST"])
def olvide_contrasena():
    if request.method == "POST":
        email = request.form["email"]
        nueva_contrasena = request.form["nueva_contrasena"]
        confirmar_contrasena = request.form["confirmar_contrasena"]

        if nueva_contrasena != confirmar_contrasena:
            flash("Las contraseñas no coinciden.")
            return redirect(url_for('olvide_contrasena_bp.olvide_contrasena'))

        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuario WHERE email = %s", (email,))
        usuario = cursor.fetchone()

        if usuario:
            nueva_hash = generate_password_hash(nueva_contrasena)
            cursor.execute("UPDATE usuario SET contrasena = %s WHERE email = %s", (nueva_hash, email))
            conexion.commit()
            flash("Tu contraseña ha sido actualizada.")
            cursor.close()
            conexion.close()
            return redirect(url_for('inicio_de_seccion_bp.inicio_de_seccion'))
        else:
            flash("No existe un usuario con ese correo.")
            cursor.close()
            conexion.close()
            return redirect(url_for('olvide_contrasena_bp.olvide_contrasena'))

    return render_template("usuarios/olvide_contrasena.html")
