from flask import Blueprint, render_template
from source.database.database import obtener_conexion 
# Define el blueprint
arboles_bp = Blueprint('arboles_bp', __name__)

# Ruta del blueprint
@arboles_bp.route('/Arboles')
def arboles():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        SELECT p.*, c.categoria 
        FROM producto p
        JOIN categoria c ON p.id_categoria = c.id_categoria
        WHERE c.categoria = %s
    """
    cursor.execute(consulta, ('Arboles',))
    arboles = cursor.fetchall()
    for producto in arboles:
        print(producto)
    return render_template('categorias/arboles.html', arboles=arboles )