from flask import Flask, render_template, url_for, request, redirect
from source.database.database import obtener_conexion #Importando conexion datebase

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
# vistas empresa
@app.route('/nosotros')
def nosotros():
    return render_template('empresa/nosotros.html')

@app.route('/contactanos')
def contactanos():
    return render_template('empresa/contactanos.html')
# Vistas para el usuario
@app.route('/inicio_de_seccion')
def inicio_de_seccion():
    return render_template('usuarios/inicio_de_seccion.html')

@app.route('/registrarse', methods = ['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        nombre          = request.form['nombre']
        apellido        = request.form['apellido']
        gmail           = request.form['gmail']
        contrasena      = request.form['contrasena']
        telefono        = request.form['telefono']
        direccion       = request.form['direccion']
        dni             = request.form['dni']
        id_tipo_usuario = 2

        conecion_database = obtener_conexion()
        miCursor = conecion_database.cursor() 

        sql = "INSERT INTO usuario(nombre_cliente, apellido_cliente, email, contrasena, telefono, direccion, dni, id_tipo_usuario) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (nombre, apellido, gmail, contrasena, telefono, direccion, dni, id_tipo_usuario)

        miCursor.execute(sql, valores)
        conecion_database.commit()

        miCursor.close()
        conecion_database.close()
    return render_template('usuarios/registrarse.html')

# Vistas para las Categorias

@app.route('/PlantasOrnamentales')
def plantas_ornamentales():
    return render_template('categorias/plantas_ornamentales.html')

@app.route('/Frutales')
def frutales():
    return render_template('categorias/frutales.html')

@app.route('/Arboles')
def arboles():
    return render_template('categorias/arboles.html')

@app.route('/Suculentas')
def suculentas():
    return render_template('categorias/suculentas.html')

@app.route('/EnredaderasTrepadorasColgantes')
def enre_plant_trepa_colgan():
    return render_template('categorias/enre_plant_trepa_colgan.html')

# Vistas para Ventas Adicionales

@app.route('/VentasAbonoSustratos')
def ventas_de_abono_sustratos():
    return render_template('ventas_adicionales/ventas_de_abono_sustratos.html')

@app.route('/VentasHerramientas')
def ventas_de_herramientas():
    return render_template('ventas_adicionales/ventas_de_herramientas.html')

# Agregar Producto

@app.route('/usuarios/admin/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre_producto = request.form['nombre']
        precio = request.form['precio']
        imagen = request.form['imagen']
        descripcion = request.form['descripcion']
        stock = request.form['stock']
        id_categoria = request.form['id_categoria']

        conecion_database = obtener_conexion()
        miCursor = conecion_database.cursor() 

        sql = "INSERT INTO producto(nombre_producto, precio, imagen, descripcion, stock, id_categoria) VALUES(%s, %s, %s, %s, %s, %s)"
        valores = (nombre_producto, precio, imagen, descripcion, stock, id_categoria)

        miCursor.execute(sql, valores)
        conecion_database.commit()

        miCursor.close()
        conecion_database.close()
    return render_template('usuarios/admin/agregar_producto.html')

# Visualizar Usuarios
@app.route('/usuarios/admin/visualizar_usuarios')
def visualizar_usuarios():
    conexion = obtener_conexion()
    miCursor = conexion.cursor(dictionary=True)  

    miCursor.execute("SELECT * FROM usuario")
    usuarios = miCursor.fetchall()

    miCursor.close()
    conexion.close()

    return render_template('usuarios/admin/visualizar_usuarios.html', usuarios=usuarios)

# Visualizar Productos
@app.route('/usuarios/admin/visualizar_productos')
def visualizar_productos():
    conexion = obtener_conexion()
    miCursor = conexion.cursor(dictionary=True)  

    miCursor.execute("SELECT * FROM producto")
    productos = miCursor.fetchall()

    miCursor.close()
    conexion.close()

    return render_template('usuarios/admin/visualizar_productos.html', productos=productos)


# Modificar Datos Usuarios
@app.route('/usuarios/<int:id_usuario>/editar', methods=['GET', 'POST'])
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
    
# Modificar Datos Productos

@app.route('/productos/<int:id_producto>/editar', methods=['GET', 'POST'])
def editar_producto(id_producto):
    conexion = obtener_conexion()
    miCursor = conexion.cursor(dictionary=True)

    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        imagen = request.form['imagen']
        descripcion = request.form['descripcion']
        stock = request.form['stock']
        id_categoria = request.form['id_categoria']

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
        valores = (nombre, precio, imagen, descripcion, stock, id_categoria, id_producto)
        miCursor.execute(sql, valores)
        conexion.commit()

        miCursor.close()
        conexion.close()
        return redirect('/usuarios/admin/visualizar_productos')

    # GET: Mostrar datos actuales
    miCursor.execute("SELECT * FROM producto WHERE id_producto = %s", (id_producto,))
    producto = miCursor.fetchone()
    miCursor.close()
    conexion.close()

    return render_template('usuarios/admin/modificar_datos_producto.html', producto=producto)


# Eliminar Datos Usuarios

@app.route('/usuarios/<int:id_usuario>/eliminar', methods=['GET', 'POST'])
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

# Eliminar Datos Productos
@app.route('/productos/<int:id_producto>/eliminar', methods=['GET', 'POST'])
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


if __name__ == '__main__':
    app.run(debug=True)