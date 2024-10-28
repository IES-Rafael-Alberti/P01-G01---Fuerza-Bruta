import hashlib
import pytest
from hash_module import hashear, comprobarDict  # Asegúrate de que el nombre del módulo sea correcto

# Función simulada para leer contraseñas
def mock_passwords_file():
    return ["123456\n", "password123\n", "qwerty\n"]

def test_hashear():
    sample_password = "password123"
    expected_hash = hashlib.sha256(sample_password.encode()).hexdigest()
    
    actual_hash = hashear(sample_password)
    assert actual_hash == expected_hash, "El hash calculado no es el esperado."

def test_comprobarDict_encontrado():
    password_to_check = "password123"
    mock_file = mock_passwords_file()

    # Simular el comportamiento de abrir un archivo
    class MockFile:
        def __init__(self, passwords):
            self.passwords = passwords
            
        def readlines(self):
            return self.passwords

    # Crear un archivo simulado con las contraseñas
    simulated_file = MockFile(mock_file.copy())

    result = comprobarDict(password_to_check, simulated_file)
    assert result == "La contraseña es: password123", "La contraseña debería haber sido encontrada."

def test_comprobarDict_no_encontrado():
    password_to_check = "wrongpassword"
    mock_file = mock_passwords_file()

    # Simular el comportamiento de abrir un archivo
    class MockFile:
        def __init__(self, passwords):
            self.passwords = passwords
            
        def readlines(self):
            return self.passwords

    # Crear un archivo simulado con las contraseñas
    simulated_file = MockFile(mock_file.copy())

    result = comprobarDict(password_to_check, simulated_file)
    assert result == "No se ha encontrado la contraseña en el diccionario", "La contraseña debería haber sido no encontrada."


if __name__ == "__main__":
    pytest.main()
