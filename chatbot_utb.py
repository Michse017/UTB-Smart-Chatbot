import re
import unicodedata
from information_base import career, graph, career_names, bfs, belongs_to_faculty
from pyDatalog import pyDatalog

# Declarar variables para PyDatalog (incluyendo X, Y, Z, F)
pyDatalog.create_terms('X, Y, Z, F')

def normalize_str(s):
    """
    Normaliza una cadena removiendo acentos y convirtiendo a minúsculas.
    """
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn').lower()

def build_normalized_graph():
    """
    Construye una versión normalizada (sin acentos) del grafo de palabras clave
    y un diccionario que mapea los nombres normalizados de carreras a su versión oficial.
    """
    norm_graph = {}
    for key, neighbors in graph.items():
        norm_key = normalize_str(key)
        norm_neighbors = [normalize_str(n) for n in neighbors]
        norm_graph[norm_key] = norm_neighbors
    norm_career_names = {}
    for name in career_names:
        norm_career_names[normalize_str(name)] = name
    return norm_graph, norm_career_names

# Construir estructuras normalizadas una sola vez
norm_graph, norm_career_names = build_normalized_graph()

def find_career(user_query):
    """
    Procesa la consulta del usuario y utiliza BFS (con el grafo normalizado)
    para determinar la carrera solicitada.
    """
    tokens = re.findall(r'\w+', user_query)
    for token in tokens:
        norm_token = normalize_str(token)
        if norm_token in norm_graph:
            found_norm = bfs(norm_graph, norm_token, set(norm_career_names.keys()))
            if found_norm:
                return norm_career_names.get(found_norm)
    return None

def get_career_info(career_name):
    """
    Consulta la base de conocimientos (hechos de PyDatalog) para obtener la información de la carrera.
    """
    result = career(career_name, X, Y, Z) # type: ignore
    for r in result:
        return r[0], r[1], r[2]
    return None

def chatbot_response(user_query):
    """
    Procesa la consulta del usuario y retorna una respuesta formateada con la información de la carrera,
    o responde de forma especial si se trata de agradecimientos o despedidas.
    """
    # Detectar palabras de agradecimiento o despedida
    lower_query = user_query.strip().lower()
    if lower_query in ["gracias", "muchas gracias", "thank you", "ty"]:
        return "¡De nada! Estoy aquí para ayudarte. Si necesitas algo más, no dudes en preguntar."
    if lower_query in ["adiós", "hasta luego", "bye"]:
        return "¡Hasta luego! Gracias por utilizar el servicio. ¡Que tengas un excelente día!"

    found_career = find_career(user_query)
    if found_career:
        info = get_career_info(found_career)
        if info:
            desc, duration, modality = info
            # Consultar la inferencia de la facultad para la carrera
            faculty_query = belongs_to_faculty(found_career, F) # type: ignore
            solutions = list(faculty_query)
            if solutions:
                if len(solutions[0]) >= 2:
                    faculty_info = solutions[0][1]
                else:
                    faculty_info = solutions[0][0]
            else:
                faculty_info = "Desconocida"
            return (f"Carrera: {found_career}\n"
                    f"Descripción: {desc}\n"
                    f"Duración: {duration}\n"
                    f"Modalidad: {modality}\n"
                    f"Pertenece a: {faculty_info}")
        else:
            return "No se encontró información para la carrera solicitada."
    else:
        return "No se encontró la carrera en la base de datos. Verifica la palabra clave de tu consulta."

def start_chat():
    print("Bienvenido al Chatbot de carreras de pregrado de la UTB.")
    print("Escribe 'salir' para terminar la conversación.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ['salir', 'exit', 'quit']:
            print("Chatbot: Gracias por usar el servicio. ¡Hasta luego!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    start_chat()
