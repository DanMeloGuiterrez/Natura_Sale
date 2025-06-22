from flask import Blueprint, render_template, request, redirect
from source.database.database import obtener_conexion 


# Define el blueprint
editar_usuario_bp = Blueprint('editar_usuario_bp', __name__)

# Ruta del blueprint
@editar_usuario_bp.route('/usuarios/<int:id_usuario>/editar', methods=['GET', 'POST'])
def editar_usuario(id_usuario):
    conexion = obtener_conexion()
    miCursor = conexion.cursor(dictionary=True)

    if request.method == 'POST':
        # 1. Obtener valores del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        dni = request.form['dni']

        # 2. Actualizar datos
        sql = """
            UPDATE usuario
            SET nombre_cliente = %s,
                apellido_cliente = %s,
                email = %s,
                telefono = %s,
                direccion = %s,
                dni = %s
            WHERE id_usuario = %s
        """
        valores = (nombre, apellido, email, telefono, direccion, dni, id_usuario)
        miCursor.execute(sql, valores)
        conexion.commit()

        miCursor.close()
        conexion.close()
        return redirect('/usuarios/admin/visualizar_usuarios')

    # GET: mostrar datos actuales
    miCursor.execute("SELECT * FROM usuario WHERE id_usuario = %s", (id_usuario,))
    usuario = miCursor.fetchone()
    miCursor.close()
    conexion.close()
    return render_template('usuarios/admin/modificar_datos_usuario.html', usuario=usuario)
    