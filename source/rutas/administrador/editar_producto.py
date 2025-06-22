from flask import Blueprint, render_template, request, redirect
from source.database.database import obtener_conexion 

from werkzeug.utils import secure_filename
import os
# Define el blueprint
editar_producto_bp = Blueprint('editar_producto_bp', __name__)

# Ruta del blueprint
@editar_producto_bp.route('/productos/<int:id_producto>/editar', methods=['GET', 'POST'])
def editar_producto(id_producto):
    conexion = obtener_conexion()
    miCursor = conexion.cursor(dictionary=True)

    # Obtener datos actuales del producto
    miCursor.execute("SELECT * FROM producto WHERE id_producto = %s", (id_producto,))
    producto = miCursor.fetchone()
    
    if request.method == 'POST':
        # Obtener valores del formulario
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = request.form['precio']
        stock = request.form['stock']
        id_categoria = request.form['id_categoria']

        # Verificar si se cargó una nueva imagen
        imagen = request.files['imagen']
        if imagen and imagen.filename != '':
            nombre_imagen = secure_filename(imagen.filename)
            ruta_imagen = os.path.join('static/img', nombre_imagen)
            imagen.save(ruta_imagen)
        else:
            nombre_imagen = producto['imagen']  # Mantener imagen anterior

        # Actualizar datos
        sql = """
            UPDATE producto
            SET nombre_producto = %s,
                precio = %s,
                imagen = %s,
                descripcion = %s,
                stock = %s,
                id_categoria = %s
            WHERE id_producto = %s
        """

        valores = (nombre, precio, nombre_imagen, descripcion, stock, id_categoria, id_producto)
        miCursor.execute(sql, valores)
        conexion.commit()

        miCursor.close()
        conexion.close()
        return redirect('/usuarios/admin/visualizar_productos')

    # GET: mostrar plantilla con datos actuales
    miCursor.close()
    conexion.close()
    return render_template("usuarios/admin/modificar_datos_producto.html", producto=producto)
