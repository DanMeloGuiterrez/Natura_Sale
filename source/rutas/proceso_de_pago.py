from flask import Blueprint, render_template, session

# Define el blueprint
proceso_de_pago_bp = Blueprint('proceso_de_pago_bp', __name__)

# Ruta del blueprint
@proceso_de_pago_bp.route('/proceso_de_pago')
def proceso_de_pago():
    return render_template(
                'usuarios/proceso_de_pago.html',
                nombre=session.get('nombre'),
                apellido=session.get('apellido'),
                email=session.get('email'),
                telefono=session.get('telefono'),
                direccion=session.get('direccion'),
                dni=session.get('dni')
            )