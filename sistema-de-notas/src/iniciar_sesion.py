from src.database import users

def login():
    print("bienvenido al sistema de notas - Iniciar sesión")
    email_stored= input("Ingresa tú correo electronico: ")
    password_stored= input("Ingresa tú contraseña: ")
    
    user_match = None
    for i in users:
        if i["email"]== email_stored and i["password"] == password_stored:
            user_match= i
            break
    
    if user_match:
        print(f"Estas logueado {user_match['name']}")
        return user_match
    else:
        print ("Usuario o contraseña incorrectos")
        input("Presiona enter para volver al menú")
        return None