from flask import Blueprint, render_template, request, redirect
from source.database.database import obtener_conexion

eliminar_producto_bp = Blueprint('eliminar_producto_bp', __name__)

@eliminar_producto_bp.route('/productos/<int:id_producto>/eliminar', methods=['GET', 'POST'])
def eliminar_producto(id_producto):
    conexion = obtener_conexion()
    miCursor = conexion.cursor(dictionary=True)

    # Obtener producto específico
    miCursor.execute("SELECT * FROM producto WHERE id_producto = %s", (id_producto,))
    producto = miCursor.fetchone()

    if request.method == 'POST':
        # Primero eliminamos los registros en productos_pedidos que usan ese producto
        miCursor.execute("DELETE FROM productos_pedidos WHERE id_producto = %s", (id_producto,))
        # Luego eliminamos el producto
        miCursor.execute("DELETE FROM producto WHERE id_producto = %s", (id_producto,))

        conexion.commit()
        miCursor.close()
        conexion.close()
        return redirect('/usuarios/admin/visualizar_productos')

    miCursor.close()
    conexion.close()
    return render_template('usuarios/admin/eliminar_producto.html', producto=producto)
