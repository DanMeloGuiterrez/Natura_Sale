from flask import Blueprint, url_for, redirect, render_template, session

# Define el blueprint
mostrar_panel_admin_bp = Blueprint('mostrar_panel_admin_bp', __name__)

# Ruta del blueprint
@mostrar_panel_admin_bp.route('/admin')
def mostrar_panel_admin():
    if 'rol' in session and session['rol'] is not None:
        return render_template(
            'usuarios/admin/perfil_administrador.html',
            nombre=session.get('nombre'),
            apellido=session.get('apellido'),
            email=session.get('email'),
            telefono=session.get('telefono'),
            direccion=session.get('direccion'),
            dni=session.get('dni')
        )
    
    return redirect(url_for('inicio_de_seccion_bp.inicio_de_seccion'))