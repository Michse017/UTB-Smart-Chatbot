from pyDatalog import pyDatalog
pyDatalog.clear()

# Declarar las variables y predicados dinámicos de PyDatalog
pyDatalog.create_terms('career, X, Y, Z, belongs_to_faculty, C, F')

# Definiciones dummy para editores (no se ejecutan)
if False:
    def career(a, b=None, c=None, d=None):
        pass
    def belongs_to_faculty(a, b=None):
        pass

# Exportamos explícitamente los nombres que se pueden importar
__all__ = ["career", "graph", "career_names", "bfs", "belongs_to_faculty"]

# ======================================================
# Función BFS para recorrer el grafo de palabras clave
# ======================================================
def bfs(graph, start, target_set):
    """
    Realiza una búsqueda en anchura (BFS) en el grafo de palabras clave.
    Retorna el nombre oficial de la carrera si se encuentra.
    """
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        node = queue.pop(0)
        if node in target_set:
            return node
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return None

# ===============================
# Facultades y Carreras
# ===============================
# Facultad de Ingeniería
# Facultad de Ingeniería, Arquitectura y Diseño
+career('Diseño',  # type: ignore
         'El programa de Diseño forma profesionales para la creación y desarrollo de soluciones en diseño, integrando aspectos de ingeniería, arquitectura y comunicación visual.',
         '9 semestres',
         'presencial')

# Escuela de Transformación Digital
+career('Marketing y Transformación Digital',  # type: ignore
         'El programa de Marketing y Transformación Digital forma profesionales en estrategias de marketing digital y procesos de transformación en entornos tecnológicos.',
         '8 semestres',
         'presencial')

+career('Ciencia de Datos',  # type: ignore
         'El programa de Ciencia de Datos capacita a los estudiantes en análisis de datos, modelado estadístico y técnicas de aprendizaje automático para la toma de decisiones basadas en información.',
         '9 semestres',
         'presencial')

+career('Ingeniería Civil',  # type: ignore
         'El programa de Ingeniería Civil forma profesionales para el diseño, construcción y mantenimiento de infraestructuras.',
         '10 semestres',
         'presencial')

+career('Ingeniería Mecánica',  # type: ignore
         'El programa de Ingeniería Mecánica se enfoca en el diseño y análisis de sistemas mecánicos.',
         '10 semestres',
         'presencial')

+career('Ingeniería Industrial',  # type: ignore
         'El programa de Ingeniería Industrial se centra en la optimización de procesos, logística y gestión de operaciones.',
         '10 semestres',
         'virtual')

+career('Ingeniería de Sistemas y Computación',  # type: ignore
         'El programa de Ingeniería de Sistemas y Computación forma profesionales en el desarrollo de software y soluciones tecnológicas.',
         '10 semestres',
         'presencial')

+career('Ingeniería Ambiental',  # type: ignore
         'El programa de Ingeniería Ambiental se orienta hacia el desarrollo sostenible y la protección del medio ambiente.',
         '10 semestres',
         'presencial')

+career('Ingeniería Biomédica',  # type: ignore
         'El programa de Ingeniería Biomédica integra principios de ingeniería y ciencias médicas para diseñar soluciones en el ámbito de la salud.',
         '10 semestres',
         'virtual')

+career('Ingeniería Electrónica',  # type: ignore
         'El programa de Ingeniería Electrónica se dedica al diseño y desarrollo de circuitos y dispositivos electrónicos.',
         '10 semestres',
         'presencial')

+career('Ingeniería Mecatrónica',  # type: ignore
         'La carrera de Ingeniería Mecatrónica integra principios de mecánica, electrónica y computación para diseñar y desarrollar sistemas automatizados e inteligentes.',
         '10 semestres',
         'presencial')

+career('Ingeniería Química',  # type: ignore
         'El programa de Ingeniería Química aplica procesos químicos para la producción de materiales y energía.',
         '10 semestres',
         'virtual')

# Facultad de Ciencias Económicas y Administrativas
+career('Administración de Empresas',  # type: ignore
         'El programa de Administración de Empresas ofrece habilidades en gestión, estrategia y liderazgo organizacional.',
         '9 semestres',
         'presencial')

+career('Economía',  # type: ignore
         'El programa de Economía estudia la producción, distribución y consumo de bienes y servicios.',
         '9 semestres',
         'presencial')

+career('Contaduría Pública',  # type: ignore
         'El programa de Contaduría Pública forma profesionales en auditoría financiera, gestión tributaria y contabilidad.',
         '9 semestres',
         'virtual')

+career('Negocios Internacionales',  # type: ignore
         'El programa de Negocios Internacionales se enfoca en el comercio global, marketing internacional y gestión intercultural.',
         '9 semestres',
         'presencial')

+career('Finanzas y Comercio Exterior',  # type: ignore
         'El programa de Finanzas y Comercio Exterior abarca la gestión financiera, inversiones y comercio internacional.',
         '9 semestres',
         'presencial')

# Facultad de Ciencias Sociales y Humanidades
+career('Derecho',  # type: ignore
         'El programa de Derecho forma profesionales en teoría, práctica y jurisprudencia legal.',
         '10 semestres',
         'presencial')

+career('Psicología',  # type: ignore
         'El programa de Psicología estudia el comportamiento humano y los procesos mentales.',
         '9 semestres',
         'virtual')

+career('Comunicación Social',  # type: ignore
         'El programa de Comunicación Social se enfoca en medios, periodismo y relaciones públicas.',
         '9 semestres',
         'virtual')

+career('Relaciones Internacionales',  # type: ignore
         'El programa de Relaciones Internacionales examina la política global, la diplomacia y las organizaciones internacionales.',
         '9 semestres',
         'presencial')


# ========================================
# Grafo de Palabras Clave para BFS Mapping
# ========================================
graph = {
    # Faculty of Engineering synonyms
    # Para la carrera "Diseño"
    'diseño': ['Diseño'],

    # Para "Marketing y Transformación Digital"
    'marketing y transformación digital': ['Marketing y Transformación Digital'],
    'marketing': ['Marketing y Transformación Digital'],
    'transformación digital': ['Marketing y Transformación Digital'],

    # Para "Ciencia de Datos"
    'ciencia de datos': ['Ciencia de Datos'],
    'datos': ['Ciencia de Datos'],
    'ciencia': ['Ciencia de Datos'],

    'ingeniería mecatrónica': ['mecatrónica', 'mecatronica'],
    'mecatrónica': ['Ingeniería Mecatrónica'],
    'mecatronica': ['Ingeniería Mecatrónica'],

    'ingeniería civil': ['civil'],
    'civil': ['Ingeniería Civil'],

    'ingeniería mecánica': ['mecánica', 'mechanical'],
    'mecánica': ['Ingeniería Mecánica'],
    'mechanical': ['Ingeniería Mecánica'],

    'ingeniería industrial': ['industrial'],
    'industrial': ['Ingeniería Industrial'],

    'ingeniería de sistemas y computación': ['sistemas', 'computación', 'sistemas y computación'],
    'sistemas': ['Ingeniería de Sistemas y Computación'],
    'computación': ['Ingeniería de Sistemas y Computación'],
    'sistemas y computación': ['Ingeniería de Sistemas y Computación'],

    'ingeniería ambiental': ['ambiental'],
    'ambiental': ['Ingeniería Ambiental'],

    'ingeniería biomédica': ['biomédica'],
    'biomédica': ['Ingeniería Biomédica'],

    'ingeniería electrónica': ['electrónica'],
    'electrónica': ['Ingeniería Electrónica'],

    'ingeniería química': ['química'],
    'química': ['Ingeniería Química'],

    # Faculty of Economic and Administrative Sciences synonyms
    'administración de empresas': ['administración', 'empresas'],
    'administración': ['Administración de Empresas'],
    'empresas': ['Administración de Empresas'],

    'economía': ['economía'],

    'contaduría pública': ['contaduría'],
    'contaduría': ['Contaduría Pública'],

    'negocios internacionales': ['negocios', 'internacionales'],
    'negocios': ['Negocios Internacionales'],
    'internacionales': ['Negocios Internacionales'],

    'finanzas y comercio exterior': ['finanzas', 'comercio exterior'],
    'finanzas': ['Finanzas y Comercio Exterior'],
    'comercio exterior': ['Finanzas y Comercio Exterior'],

    # Faculty of Social Sciences and Humanities synonyms
    'derecho': ['derecho'],
    'psicología': ['psicología'],
    'comunicación social': ['comunicación'],
    'comunicación': ['Comunicación Social'],
    'relaciones internacionales': ['relaciones internacionales', 'relaciones'],
    'relaciones': ['Relaciones Internacionales']
}

career_names = {
    'Diseño',
    'Marketing y Transformación Digital',
    'Ciencia de Datos',
    'Ingeniería Civil',
    'Ingeniería Mecánica',
    'Ingeniería Industrial',
    'Ingeniería de Sistemas y Computación',
    'Ingeniería Ambiental',
    'Ingeniería Biomédica',
    'Ingeniería Electrónica',
    'Ingeniería Mecatrónica',
    'Ingeniería Química',
    'Administración de Empresas',
    'Economía',
    'Contaduría Pública',
    'Negocios Internacionales',
    'Mercadeo y Negocios Globales',
    'Finanzas y Comercio Exterior',
    'Derecho',
    'Psicología',
    'Comunicación Social',
    'Relaciones Internacionales'
}

# ========================================
# Regla: Inferir la facultad a la que pertenece cada carrera
# ========================================
def determine_faculty(career_name):
    if career_name.startswith("Ingeniería"):
        return "Faculty of Engineering"
    elif career_name in ["Administración de Empresas", "Economía", "Contaduría Pública", 
                         "Negocios Internacionales", "Mercadeo y Negocios Globales", "Finanzas y Comercio Exterior"]:
        return "Faculty of Economic and Administrative Sciences"
    elif career_name in ["Derecho", "Psicología", "Comunicación Social", "Relaciones Internacionales"]:
        return "Faculty of Social Sciences and Humanities"
    else:
        return "Unknown"

# Se usa X, Y, Z para los argumentos no utilizados
belongs_to_faculty(C, F) <= career(C, X, Y, Z) & (F == determine_faculty(C)) # type: ignore

if __name__ == "__main__":
    print("Information Base Loaded")
    # Ejemplo: mostrar la facultad inferida para cada carrera
    query = belongs_to_faculty(C, F) # type: ignore
    for answer in query:
        print("    ")
        print("Career:", answer[0], "-> Faculty:", answer[1])
