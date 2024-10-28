import hashlib

#Funcion para hashear en SHA256
def hashear(cadena):
    cadena_to_bytes = hashlib.sha256(cadena.encode())  
    bytes_to_hex = cadena_to_bytes.hexdigest()
    return bytes_to_hex 

def comprobarDict(cadena, dict):
    pass

if __name__ == "__main__":
    password = input("Introduce tu contraseña: ")