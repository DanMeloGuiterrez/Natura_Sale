from flask import Blueprint, render_template
from source.database.database import obtener_conexion 

# Define el blueprint
plantas_ornamentales_bp = Blueprint('plantas_ornamentales_bp', __name__)

# Ruta del blueprint

@plantas_ornamentales_bp.route('/PlantasOrnamentales')
def plantas_ornamentales():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        SELECT p.*, c.categoria 
        FROM producto p
        JOIN categoria c ON p.id_categoria = c.id_categoria
        WHERE c.categoria = %s
    """
    cursor.execute(consulta, ("Plantas Ornamentales",))
    productos = cursor.fetchall()

    return render_template('categorias/plantas_ornamentales.html', productos=productos)

