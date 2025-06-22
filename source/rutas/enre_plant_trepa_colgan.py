from flask import Blueprint, render_template
from source.database.database import obtener_conexion 

# Define el blueprint
enre_plant_trepa_colgan_bp = Blueprint('enre_plant_trepa_colgan_bp', __name__)

# Ruta del blueprint
@enre_plant_trepa_colgan_bp.route('/EnredaderasTrepadorasColgantes')
def enre_plant_trepa_colgan():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    consulta = """
        SELECT p.*, c.categoria 
        FROM producto p
        JOIN categoria c ON p.id_categoria = c.id_categoria
        WHERE c.categoria = %s
    """
    cursor.execute(consulta, ("Enredaderas, plantas trepadoras y colgantes",))
    enre_plant_trepa_colgan = cursor.fetchall()
    return render_template('categorias/enre_plant_trepa_colgan.html', enre_plant_trepa_colgan= enre_plant_trepa_colgan)
