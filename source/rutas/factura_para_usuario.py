from flask import Blueprint, session
from source.database.database import obtener_conexion

factura_para_usuario_bp = Blueprint('factura_para_usuario_bp', __name__)

@factura_para_usuario_bp.route('/factura_para_usuario_bp')
def factura_para_usuario():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        id_usuario = session['id_usuario']  # Suponiendo que guardas el id del usuario en sesión al hacer login
        cursor.execute("INSERT INTO factura (id_usuario) VALUES (%s)", (id_usuario,))
        conexion.commit()