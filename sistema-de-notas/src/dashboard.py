from src.database import students

def registrar_notas():
    print("\n=== Registro de notas ===")
    
    nombre = input("Ingrese el nombre del estudiante: ")
    
    materias = {
        "Web 2": [],
        "Nuevas Tecnologias": [],
        "Backend 2": []
    }
    
    promedios = {}
    
    for materia in materias:
        print(f"\nIngresando notas para {materia}")
        
        for i in range(1, 4):
            nota = float(input(f"Ingrese nota {i}: "))
            materias[materia].append(nota)
        
        promedio = sum(materias[materia]) / 3
        promedios[materia] = promedio
        
        print(f"Promedio de {materia}: {promedio}")
    
    estudiante = {
        "nombre": nombre,
        "materias": materias,
        "promedios": promedios
    }
    
    students.append(estudiante)
    
    print("\nEstudiante guardado correctamente.")
    input("Presiona Enter para continuar...")
