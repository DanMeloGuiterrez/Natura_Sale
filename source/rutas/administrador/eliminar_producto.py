from flask import Blueprint, render_template, request, redirect
from source.database.database import obtener_conexion 

# Define el blueprint
eliminar_producto_bp = Blueprint('eliminar_producto_bp', __name__)

# Ruta del blueprint
@eliminar_producto_bp.route('/productos/<int:id_producto>/eliminar', methods=['GET', 'POST'])
def eliminar_producto(id_producto):
    conexion = obtener_conexion()
    miCursor = conexion.cursor(dictionary=True)

    # Obtener producto específico
    miCursor.execute("SELECT * FROM producto WHERE id_producto = %s", (id_producto,))
    producto = miCursor.fetchone()

    if request.method == 'POST':
        miCursor.execute("DELETE FROM producto WHERE id_producto = %s", (id_producto,))
        conexion.commit()
        miCursor.close()
        conexion.close()
        return redirect('/usuarios/admin/visualizar_productos')

    miCursor.close()
    conexion.close()
    return render_template('usuarios/admin/eliminar_producto.html', producto=producto)
