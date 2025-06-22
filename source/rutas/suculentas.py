from flask import Blueprint, render_template
from source.database.database import obtener_conexion 
# Define el blueprint
suculentas_bp = Blueprint('suculentas_bp', __name__)

# Ruta del blueprint
@suculentas_bp.route('/Suculentas')
def suculentas():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        SELECT p.*, c.categoria 
        FROM producto p
        JOIN categoria c ON p.id_categoria = c.id_categoria
        WHERE c.categoria = %s
    """
    cursor.execute(consulta, ("Suculentas",))
    suculentas = cursor.fetchall()
    return render_template('categorias/suculentas.html', suculentas=suculentas)