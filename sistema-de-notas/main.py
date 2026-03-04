from src.registroUsuario import registro
from src.iniciarSesion import iniciarsesion 
from src.visualizar import visualizar_notas
from src.dashboard import registrar_notas
from src.database import students


def menu():
    while True:
        print("\n       Bienvenido \n Selecciona una de las siguientes opciones:  \n\n 1. Registrar Usuario \n 2. Iniciar Sesión \n 3. Ver notas \n 4. Salir")
        
        opcion= input("\n Selecciona una opción:")
        if opcion == "1":
            registro()  
            
        elif opcion =="2":
            user_logueado= iniciarsesion()
            if user_logueado:
                registrar_notas(user_logueado)

        elif opcion == "3":
            if not students: 
                print("\n Aún no hay registros de estudiantes.")
            else:
                visualizar_notas(students)

        elif opcion == "4":
            print("\n Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("\n[!] Opción no válida. Inténtalo de nuevo.")
            input("Presiona Enter para continuar")
            
if __name__ == "__main__":
    menu()