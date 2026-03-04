from src.database import students

def visualizar_notas():
    print("\n=== LISTA DE ESTUDIANTES ===")
    
    if not students:
        print("No hay estudiantes registrados.")
        return
    
    for estudiante in students:
        print("\n---------------------------")
        print(f"Estudiante: {estudiante['nombre']}")
        
        for materia in estudiante["materias"]:
            print(f"\nMateria: {materia}")
            print(f"Notas: {estudiante['materias'][materia]}")
            print(f"Promedio: {estudiante['promedios'][materia]}")
