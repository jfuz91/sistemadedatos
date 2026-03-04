import src.database as db

def registrar_notas(user_logueado):
    while True:
        nombre = input("\nIngrese el nombre del estudiante: ")
        
        materias = {
            "Web 2": [],
            "Nuevas Tecnologias": [],
            "Backend 2": []
        }
        
        promedios = {}
        
        for materia in materias:
            print(f"\n ingrese notas para {materia}")
            
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
        
        db.students.append(estudiante)
        
        print(f"\nEstudiante {nombre} guardado correctamente")
        
        
        continuar = input("\n¿Desea registrar otro estudiante? (s/n): ").lower()
        
        if continuar != "s":
            print("Regresando al menú...")
            break 