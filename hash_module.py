import hashlib

#Funcion para hashear en SHA256
def hashear(cadena):
    cadena_to_bytes = hashlib.sha256(cadena.encode())  
    bytes_to_hex = cadena_to_bytes.hexdigest()
    return bytes_to_hex 

def comprobarDict(cadena, dict):
    passwords_list = [linea.rstrip() for linea in dict.readlines()]
    for password in passwords_list:
        password_hasheada = hashear(password)
        if cadena == password_hasheada:
            return f"La contraseña para el hash {cadena} es {password}"
    return "No se ha encontrado la contraseña en el diccionario"

    
    

if __name__ == "__main__":
    passwords_file = open("passwords.txt") 
    password_input = input("Introduce la contraseña que quieres comprobar: ")
    print(hashear(password_input))
    print(comprobarDict(password_input, passwords_file))
