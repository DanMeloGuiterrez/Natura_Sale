from flask import Blueprint, render_template, request, redirect
from source.database.database import obtener_conexion

eliminar_usuario_bp = Blueprint('eliminar_usuario_bp', __name__)

@eliminar_usuario_bp.route('/usuarios/<int:id_usuario>/eliminar', methods=['GET', 'POST'])
def eliminar_usuario(id_usuario):
    conexion = obtener_conexion()
    miCursor = conexion.cursor(dictionary=True)

    # Verificar si el usuario existe
    miCursor.execute("SELECT * FROM usuario WHERE id_usuario = %s", (id_usuario,))
    usuario = miCursor.fetchone()

    if request.method == 'POST':
        # Obtener todas las facturas del usuario
        miCursor.execute("SELECT id_factura FROM factura WHERE id_usuario = %s", (id_usuario,))
        facturas = miCursor.fetchall()

        # Eliminar los registros en productos_pedidos relacionados con las facturas
        for factura in facturas:
            miCursor.execute("DELETE FROM productos_pedidos WHERE id_factura = %s", (factura['id_factura'],))

        # Eliminar facturas del usuario
        miCursor.execute("DELETE FROM factura WHERE id_usuario = %s", (id_usuario,))
        # Eliminar usuario
        miCursor.execute("DELETE FROM usuario WHERE id_usuario = %s", (id_usuario,))

        conexion.commit()

        miCursor.close()
        conexion.close()
        return redirect('/usuarios/admin/visualizar_usuarios')

    miCursor.close()
    conexion.close()
    return render_template('usuarios/admin/eliminar_usuario.html', usuario=usuario)
