from src.database import users

def registro ():
    print("\n -Registro de usuario-")
    name = input("\nIngresa tú nombre: ")
    email= input("Ingresa tú email: ")
    password= input("Ingresa tu contraseña: ")
    
    new_user={
        "name": name,
        "email": email,
        "password": password
    }
    users.append(new_user)
    print("Registro exitoso")
    return True