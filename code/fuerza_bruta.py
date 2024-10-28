import hashlib

#Funcion para hashear en SHA256
def hashear(cadena):
    cadena_to_bytes = hashlib.sha256(cadena.encode())  
    bytes_to_hex = cadena_to_bytes.hexdigest()
    return bytes_to_hex 

def comprobarDict(cadena, dict):
    cadena_hasheada = hashear(cadena)
    passwords_list = [linea.rstrip() for linea in dict.readlines()]
    for password in passwords_list:
        password_hasheada = hashear(password)
        if cadena_hasheada == password_hasheada:
            return f"La contraseña es: {password}"
    return "No se ha encontrado la contraseña en el diccionario"

    
    

if __name__ == "__main__":
    passwords_file = open("passwords.txt") 
    password_input = input("Introduce la contraseña que quieres comprobar: ")
    print(comprobarDict(password_input, passwords_file))