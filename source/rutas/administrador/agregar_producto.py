from flask import Blueprint, render_template, request, session, redirect, url_for
from source.database.database import obtener_conexion 

from werkzeug.utils import secure_filename
import os

# Define el blueprint
agregar_producto_bp = Blueprint('agregar_producto_bp', __name__)

# Ruta del blueprint
@agregar_producto_bp.route('/usuarios/admin/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    # Verificación de rol
    if 'rol' not in session or session['rol'] != 1:
        return redirect(url_for('inicio_de_seccion_bp.inicio_de_seccion'))  # Bloquea acceso a usuarios comunes

    if request.method == 'POST':
        nombre_producto = request.form['nombre']
        precio = request.form['precio']
        descripcion = request.form['descripcion']
        stock = request.form['stock']
        id_categoria = request.form['id_categoria']

        imagen = request.files['imagen'] 

        if imagen and imagen.filename != '':
            nombre_imagen = secure_filename(imagen.filename)
            ruta_imagen = os.path.join('static/img', nombre_imagen)
            imagen.save(ruta_imagen)
        else:
            nombre_imagen = None

        conexion_database = obtener_conexion()
        miCursor = conexion_database.cursor()

        sql = "INSERT INTO producto(nombre_producto, precio, imagen, descripcion, stock, id_categoria) VALUES(%s, %s, %s, %s, %s, %s)"
        valores = (nombre_producto, precio, nombre_imagen, descripcion, stock, id_categoria)

        miCursor.execute(sql, valores)
        conexion_database.commit()
        miCursor.close()
        conexion_database.close()

    return render_template('usuarios/admin/agregar_producto.html')
