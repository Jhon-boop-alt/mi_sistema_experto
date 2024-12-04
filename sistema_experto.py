class SistemaExpertoRiesgoAcademico:
    def __init__(self, asistencia, promedio, participacion, omision_evaluaciones, problemas_socioeconomicos=False, carga_academica=None, semestre_pasado=None):
        self.asistencia = asistencia
        self.promedio = promedio  # Promedio en una escala de 0 a 20
        self.participacion = participacion
        self.omision_evaluaciones = omision_evaluaciones
        self.problemas_socioeconomicos = problemas_socioeconomicos
        self.carga_academica = carga_academica
        self.semestre_pasado = semestre_pasado

    def evaluar_riesgo(self):
        # Evaluación de riesgo por omisión de evaluaciones importantes
        if self.omision_evaluaciones >= 25:
            return self.regla_riesgo_falta_participacion()

        # Regla para Riesgo Muy Alto
        if self.asistencia < 50 and self.promedio < 10 and self.participacion < 40:
            return self.regla_riesgo_muy_alto()

        # Regla para Riesgo Alto
        if self.asistencia < 70 and self.promedio < 12 or self.participacion < 50:
            return self.regla_riesgo_alto()

        # Regla para Riesgo Medio
        if 70 <= self.asistencia <= 80 or 12 <= self.promedio <= 14 or self.promedio < self.semestre_pasado:
            return self.regla_riesgo_medio()

        # Regla para Riesgo Bajo
        if self.asistencia > 80 and self.promedio > 14 and self.participacion > 70:
            return self.regla_riesgo_bajo()

        # Si no se detecta ningún riesgo
        return {
            "Solicitud": "No se ha identificado un riesgo significativo",
            "Acción": "Continuar monitoreando el desempeño y motivar al estudiante a mantener su rendimiento"
        }

    def regla_riesgo_muy_alto(self):
        return {
            "Solicitud": "Riesgo Muy Alto",
            "Acción": "Generar alerta urgente. Recomendar intervención académica personalizada, ajustes en la carga académica y apoyo psicológico."
        }

    def regla_riesgo_alto(self):
        return {
            "Solicitud": "Riesgo Alto",
            "Acción": "Generar alerta crítica. Recomendar tutorías personalizadas, ajustes en el plan de estudios o apoyo psicológico."
        }

    def regla_riesgo_medio(self):
        return {
            "Solicitud": "Riesgo Medio",
            "Acción": "Generar alerta moderada. Sugerir sesiones grupales de refuerzo académico y una evaluación de los hábitos de estudio."
        }

    def regla_riesgo_bajo(self):
        return {
            "Solicitud": "Riesgo Bajo",
            "Acción": "No generar alerta. Continuar monitoreando el desempeño del estudiante."
        }

    def regla_riesgo_falta_participacion(self):
        return {
            "Solicitud": "Riesgo por Falta de Participación",
            "Acción": "Generar alerta específica sobre la falta de participación en evaluaciones importantes."
        }
