from flask import Blueprint, render_template
from source.database.database import obtener_conexion 
# Define el blueprint
frutales_bp = Blueprint('frutales_bp', __name__)

# Ruta del blueprint
@frutales_bp.route('/Frutales')
def frutales():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        SELECT p.*, c.categoria 
        FROM producto p
        JOIN categoria c ON p.id_categoria = c.id_categoria
        WHERE c.categoria = %s
    """
    cursor.execute(consulta, ("Frutales",))
    frutales = cursor.fetchall()
    return render_template('categorias/frutales.html', frutales=frutales)