from flask import Blueprint, render_template
from source.database.database import obtener_conexion 

# Define el blueprint
ventas_de_herramientas_bp = Blueprint('ventas_de_herramientas_bp', __name__)

# Ruta del blueprint
@ventas_de_herramientas_bp.route('/VentasHerramientas')
def ventas_de_herramientas():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        SELECT p.*, c.categoria 
        FROM producto p
        JOIN categoria c ON p.id_categoria = c.id_categoria
        WHERE c.categoria = %s
    """
    cursor.execute(consulta, ("Ventas de Herramientas y Macetas",))
    ventas_de_herramientas = cursor.fetchall()
    return render_template('ventas_adicionales/ventas_de_herramientas.html', ventas_de_herramientas=ventas_de_herramientas)
