from flask import Blueprint, render_template, session
from source.database.database import obtener_conexion

historial_compras_bp = Blueprint('historial_compras_bp', __name__)

@historial_compras_bp.route('/historial_compras')
def historial_compras():
    id_usuario = session['id_usuario']
    conexion = obtener_conexion()
    with conexion.cursor(dictionary=True) as cursor:
        cursor.execute("""
            SELECT pp.fecha_envio, p.nombre_producto AS nombre_producto, 
                pp.cantidad, pp.precio_subtotal
            FROM productos_pedidos pp
            JOIN producto p ON pp.id_producto = p.id_producto
            JOIN factura f ON pp.id_factura = f.id_factura
            WHERE f.id_usuario = %s
            ORDER BY pp.fecha_envio DESC
        """, (id_usuario,))

        historial = cursor.fetchall()
    return render_template('usuarios/historial_compras.html', historial=historial)


