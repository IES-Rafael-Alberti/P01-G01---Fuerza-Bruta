import hashlib

#SHA256
def hashear(cadena):
    cadena_to_bytes = hashlib.sha256(cadena.encode())  
    bytes_to_hex = cadena_to_bytes.hexdigest()
    return bytes_to_hex 


def comprobarDict(cadena, diccionario):
    passwords_file.seek(0)
    passwords_list = [linea.rstrip() for linea in diccionario.readlines()]
    for password in passwords_list:
        password_hasheada = hashear(password)
        if cadena == password_hasheada:
            return True
    return False

    
    

if __name__ == "__main__":
    passwords_file = open("passwords.txt") 
    password_input = input("Introduce la contraseña que quieres comprobar: ")
    if comprobarDict(password_input, passwords_file) == True:
        print("Tu contraseña no es segura porque se encuentra en el diccionario")
    else:
        print("Tu contraseña es segura y no aparece en el diccionario")
