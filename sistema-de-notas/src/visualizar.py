from src.database import students

def visualizar_notas(lista_estudiantes=None):
    if lista_estudiantes is None:
        from src.database import students
        lista_estudiantes = students

    print("\n -Lista de estudiantes-")
    
    if not lista_estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    for estudiante in lista_estudiantes :
        print(f"\n -Estudiante: {estudiante['nombre']}-")
        
        for materia in estudiante["materias"]:
            print(f"\n Materia: {materia}")
            print(f"Notas: {estudiante['materias'][materia]}")
            print(f"Promedio: {estudiante['promedios'][materia]}")
