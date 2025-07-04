from flask import Blueprint, render_template
from source.database.database import obtener_conexion 

buscador_bp = Blueprint('buscador_bp', __name__)

@buscador_bp.route('/Buscador')
def buscador():
    conexion = obtener_conexion()
    with conexion.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT id_producto, nombre_producto, precio, imagen, stock FROM producto")
        productos = cursor.fetchall()
    return render_template("usuarios/buscador.html", productos=productos)
