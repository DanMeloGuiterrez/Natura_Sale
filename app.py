from flask import Flask, render_template
#Funciones
from source.rutas.inicio_de_seccion import inicio_de_seccion_bp
from source.rutas.registrarse import registrarse_bp
<<<<<<< HEAD

=======
# Admin
>>>>>>> recuperar_codigo_mejorado
from source.rutas.administrador.verificar_rol import verificar_rol_bp
from source.rutas.administrador.cerrar_sesion import cerrar_sesion_bp
from source.rutas.administrador.mostrar_panel_admin import mostrar_panel_admin_bp
from source.rutas.mostrar_panel_usuario import mostrar_panel_usuario_bp
<<<<<<< HEAD

=======
# Cateogria
>>>>>>> recuperar_codigo_mejorado
from source.rutas.plantas_ornamentales import plantas_ornamentales_bp
from source.rutas.frutales import frutales_bp
from source.rutas.arboles import arboles_bp
from source.rutas.suculentas import suculentas_bp
from source.rutas.enre_plant_trepa_colgan import enre_plant_trepa_colgan_bp

from source.rutas.ventas_de_abono_sustratos import ventas_de_abono_sustratos_bp
from source.rutas.ventas_de_herramientas import ventas_de_herramientas_bp
<<<<<<< HEAD

=======
# Admin
>>>>>>> recuperar_codigo_mejorado
from source.rutas.administrador.agregar_producto import agregar_producto_bp

from source.rutas.administrador.visualizar_usuarios import visualizar_usuarios_bp

from source.rutas.administrador.visualizar_productos import visualizar_productos_bp

from source.rutas.administrador.editar_usuario import editar_usuario_bp

from source.rutas.administrador.editar_producto import editar_producto_bp

from source.rutas.administrador.eliminar_usuario import eliminar_usuario_bp

from source.rutas.administrador.eliminar_producto import eliminar_producto_bp

from source.rutas.proceso_de_pago import proceso_de_pago_bp
<<<<<<< HEAD
=======

>>>>>>> recuperar_codigo_mejorado

app = Flask(__name__)
app.secret_key = 'secret_key' 
# Funciones de la Pagina
app.register_blueprint(verificar_rol_bp)
app.register_blueprint(cerrar_sesion_bp)
app.register_blueprint(mostrar_panel_admin_bp)
app.register_blueprint(mostrar_panel_usuario_bp)

# Funciones para el Usuario
app.register_blueprint(inicio_de_seccion_bp)
app.register_blueprint(registrarse_bp)

# Vistas para las Categorias
app.register_blueprint(plantas_ornamentales_bp)
app.register_blueprint(frutales_bp)
app.register_blueprint(arboles_bp)
app.register_blueprint(suculentas_bp)
app.register_blueprint(enre_plant_trepa_colgan_bp)

# Vistas para Ventas Adicionales
app.register_blueprint(ventas_de_abono_sustratos_bp)
app.register_blueprint(ventas_de_herramientas_bp)

# Agregar Producto
app.register_blueprint(agregar_producto_bp)

# Visualizar Usuarios
app.register_blueprint(visualizar_usuarios_bp)

# Visualizar Productos
app.register_blueprint(visualizar_productos_bp)

# Modificar Datos Usuarios
app.register_blueprint(editar_usuario_bp)

# Modificar Datos Productos
app.register_blueprint(editar_producto_bp)

# Eliminar Datos Usuarios
app.register_blueprint(eliminar_usuario_bp)

# Eliminar Datos Productos
app.register_blueprint(eliminar_producto_bp)

# Eliminar Datos Productos
app.register_blueprint(proceso_de_pago_bp)


app.secret_key = 'secret_key' 
# Funciones de la Pagina
app.register_blueprint(verificar_rol_bp)
app.register_blueprint(cerrar_sesion_bp)
app.register_blueprint(mostrar_panel_admin_bp)
app.register_blueprint(mostrar_panel_usuario_bp)

# Funciones para el Usuario
app.register_blueprint(inicio_de_seccion_bp)
app.register_blueprint(registrarse_bp)

# Vistas para las Categorias
app.register_blueprint(plantas_ornamentales_bp)
app.register_blueprint(frutales_bp)
app.register_blueprint(arboles_bp)
app.register_blueprint(suculentas_bp)
app.register_blueprint(enre_plant_trepa_colgan_bp)

# Vistas para Ventas Adicionales
app.register_blueprint(ventas_de_abono_sustratos_bp)
app.register_blueprint(ventas_de_herramientas_bp)

# Agregar Producto
app.register_blueprint(agregar_producto_bp)

# Visualizar Usuarios
app.register_blueprint(visualizar_usuarios_bp)

# Visualizar Productos
app.register_blueprint(visualizar_productos_bp)

# Modificar Datos Usuarios
app.register_blueprint(editar_usuario_bp)

# Modificar Datos Productos
app.register_blueprint(editar_producto_bp)

# Eliminar Datos Usuarios
app.register_blueprint(eliminar_usuario_bp)

# Eliminar Datos Productos
app.register_blueprint(eliminar_producto_bp)

# Eliminar Datos Productos
app.register_blueprint(proceso_de_pago_bp)

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

if __name__ == '__main__':
    app.run(debug=True)