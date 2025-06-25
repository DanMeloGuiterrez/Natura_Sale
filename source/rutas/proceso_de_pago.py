from flask import Blueprint, render_template, session, redirect, url_for

# Define el blueprint
proceso_de_pago_bp = Blueprint('proceso_de_pago_bp', __name__)

# Ruta del blueprint
@proceso_de_pago_bp.route('/proceso_de_pago')
def proceso_de_pago():
    if 'rol' not in session:
        return redirect(url_for('inicio_de_seccion_bp.inicio_de_seccion'))

    return render_template(
        'usuarios/proceso_de_pago.html',
        nombre=session.get('nombre'),
        apellido=session.get('apellido'),
        email=session.get('email'),
        telefono=session.get('telefono'),
        direccion=session.get('direccion'),
        dni=session.get('dni')
    )
