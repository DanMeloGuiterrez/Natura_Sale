from flask import Blueprint, render_template, session, redirect, url_for
from source.database.database import obtener_conexion

visualizar_historial_compras_bp = Blueprint('visualizar_historial_compras_bp', __name__)

@visualizar_historial_compras_bp.route('/usuarios/admin/visualizar_historial_compras')
def visualizar_historial_compras():
    if 'rol' not in session or session['rol'] != 1:
        return redirect(url_for('inicio_de_seccion_bp.inicio_de_seccion'))

    conexion = obtener_conexion()
    with conexion.cursor(dictionary=True) as cursor:
        cursor.execute("""
            SELECT 
                pp.id_productos_pedidos,
                u.nombre_cliente AS nombre_usuario,
                u.apellido_cliente AS apellido_usuario,
                p.nombre_producto,
                pp.cantidad,
                pp.precio_subtotal,
                pp.fecha_envio,
                f.id_factura
            FROM productos_pedidos pp
            JOIN factura f ON pp.id_factura = f.id_factura
            JOIN usuario u ON f.id_usuario = u.id_usuario
            JOIN producto p ON pp.id_producto = p.id_producto
            ORDER BY pp.fecha_envio DESC
        """)

        historial = cursor.fetchall()

    return render_template('usuarios/admin/visualizar_historial_compras.html', historial=historial)
