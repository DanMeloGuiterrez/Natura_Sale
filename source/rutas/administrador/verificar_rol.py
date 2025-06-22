from flask import Blueprint, url_for, redirect, session, render_template

# Define el blueprint
verificar_rol_bp = Blueprint('verificar_rol_bp', __name__)

# Ruta del blueprint
@verificar_rol_bp.route('/login/verificar_rol', methods=['GET', 'POST'])
def verificar_rol():
    if 'rol' in session and session['rol'] is not None:
        if session['rol'] == 1:
            return redirect(url_for('mostrar_panel_admin_bp.mostrar_panel_admin'))  # Admin
        else:
            return redirect(url_for('mostrar_panel_usuario_bp.mostrar_panel_usuario'))  # Usuario común
    else:
        return redirect(url_for('inicio_de_seccion'))
