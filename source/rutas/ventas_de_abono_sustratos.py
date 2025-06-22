from flask import Blueprint, render_template
from source.database.database import obtener_conexion 

# Define el blueprint
ventas_de_abono_sustratos_bp = Blueprint('ventas_de_abono_sustratos_bp', __name__)

# Ruta del blueprint

@ventas_de_abono_sustratos_bp.route('/VentasAbonoSustratos')
def ventas_de_abono_sustratos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        SELECT p.*, c.categoria 
        FROM producto p
        JOIN categoria c ON p.id_categoria = c.id_categoria
        WHERE c.categoria = %s
    """
    cursor.execute(consulta, ("Venta de Abono y Sustratos",))
    ventas_de_abono_sustratos = cursor.fetchall()
    return render_template('ventas_adicionales/ventas_de_abono_sustratos.html', ventas_de_abono_sustratos = ventas_de_abono_sustratos)
