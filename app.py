from flask import Flask, render_template, request
from sistema_experto import SistemaExpertoRiesgoAcademico

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Carga el formulario

@app.route('/resultados', methods=['POST'])  # Asegúrate de que esta ruta sea 'POST'
def resultados():
    # Obtener los datos del formulario
    try:
        asistencia = float(request.form['asistencia'])
        promedio = float(request.form['promedio'])
        participacion = float(request.form['participacion'])
        omision_evaluaciones = float(request.form['omision_evaluaciones'])
        problemas_socioeconomicos = request.form['problemas_socioeconomicos'] == 'si'
        carga_academica = float(request.form['carga_academica']) if request.form['carga_academica'] else None
        semestre_pasado = float(request.form['semestre_pasado'])

        # Crear el objeto del sistema experto
        estudiante = SistemaExpertoRiesgoAcademico(
            asistencia, promedio, participacion, omision_evaluaciones, problemas_socioeconomicos, carga_academica, semestre_pasado
        )

        # Evaluar el riesgo
        resultado = estudiante.evaluar_riesgo()

        # Mostrar el resultado en una página
        return render_template('resultados.html', resultado=resultado)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
