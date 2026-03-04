from src.registroUsuario import registro
from src.iniciarSesion import iniciarsesion 
from src.visualizar import visualizar_notas
from src.dashboard import registrar_notas

def menu():
    while True:
        print("Bienvenido \n Selecciona una de las siguientes opciones: \n 1. Registrar Usuario \n 2. Iniciar Sesión \n 3. Ver notas")
        
        opcion= input("\n Seleeciona una opción:")
        if opcion == "1":
            registro()  
            
        elif opcion =="2":
            user_logueado= iniciarsesion()
            if user_logueado:
                registrar_notas(user_logueado)

        elif opcion =="3":
            visualizar_notas()
        else:
            print("\n[!] Opción no válida. Inténtalo de nuevo.")
            input("Presiona Enter para continuar")
            
if __name__ == "__main__":
    menu()