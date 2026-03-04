from src.database import users
from src.dashboard import registrar_notas

def iniciarsesion():
    print("\n -Iniciar sesión-")
    email_stored= input("\n Ingresa tú correo electronico: ")
    password_stored= input("Ingresa tú contraseña: ")
    
    user_match = None
    for i in users:
        if i["email"]== email_stored and i["password"] == password_stored:
            user_match= i
            break
    
    if user_match:
        print(f"Bienvenido profesor/a)")
        registrar_notas(user_match)
        
    else:
        print ("Usuario o contraseña incorrectos")
        input("Presiona enter para volver al menú")
        return None