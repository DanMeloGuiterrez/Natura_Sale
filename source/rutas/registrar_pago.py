from flask import Blueprint, session, request, render_template, redirect, url_for
import json
from datetime import datetime
from source.database.database import obtener_conexion

registrar_pago_bp = Blueprint('registrar_pago_bp', __name__)

@registrar_pago_bp.route('/registrar_pago', methods=['POST'])
def registrar_pago():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        id_usuario = session['id_usuario']
        carrito = json.loads(request.form['carrito_json'])

        # Capturar fecha y hora actual
        fecha_envio = datetime.now()

        # Insertar factura
        cursor.execute("INSERT INTO factura (id_usuario) VALUES (%s)", (id_usuario,))
        id_factura = cursor.lastrowid

        # Insertar productos
        for item in carrito:
            id_producto = int(item['id'])
            id_promocion = item.get('id_promocion')
            cantidad = int(item.get('cantidad', 1))
            precio = float(item.get('precio', 0))
            subtotal = float(item.get('subtotal', cantidad * precio))

            cursor.execute("""
                INSERT INTO productos_pedidos (
                    id_producto, id_factura, id_promocion,
                    cantidad, fecha_envio, precio_subtotal
                ) VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                id_producto, id_factura, id_promocion,
                cantidad, fecha_envio, subtotal
            ))

        conexion.commit()

    return redirect(url_for('historial_compras_bp.historial_compras'))
