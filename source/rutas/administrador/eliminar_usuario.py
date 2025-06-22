from flask import Blueprint, render_template, request, redirect
from source.database.database import obtener_conexion 

# Define el blueprint
eliminar_usuario_bp = Blueprint('eliminar_usuario_bp', __name__)

# Ruta del blueprint
@eliminar_usuario_bp.route('/usuarios/<int:id_usuario>/eliminar', methods=['GET', 'POST'])
def eliminar_usuario(id_usuario):
    conexion = obtener_conexion()
    miCursor = conexion.cursor(dictionary=True)  # ← Aquí está el cambio

    # Verificamos si el usuario existe
    miCursor.execute("SELECT * FROM usuario WHERE id_usuario = %s", (id_usuario,))
    usuario = miCursor.fetchone()

    if request.method == 'POST':
        miCursor.execute("DELETE FROM usuario WHERE id_usuario = %s", (id_usuario,))
        conexion.commit()
        miCursor.close()
        conexion.close()
        return redirect('/usuarios/admin/visualizar_usuarios')

    miCursor.close()
    conexion.close()
    return render_template('usuarios/admin/eliminar_usuario.html', usuario=usuario)
