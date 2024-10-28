import hashlib
import pytest
from hash_module import hash_calculator, find_password 


# Función simulada para leer contraseñas
def read_passwords():
    return ["123456", "password123", "qwerty"]

def test_hash_calculator():
    sample_password = "password123"
    expected_hash = hashlib.sha256(sample_password.encode("utf-8")).hexdigest()

    # Comprobamos que la función hash_calculator devuelva el hash esperado
    actual_hash = hash_calculator(sample_password)
    assert actual_hash == expected_hash, "El hash calculado no es el esperado."

def test_find_password():
    target_password = "password123"
    coded_target_password = hashlib.sha256(target_password.encode("utf-8")).hexdigest()

    # Reemplazar la función read_text en find_password
    found_password = find_password(coded_target_password, read_passwords)
    
    assert found_password.strip() == target_password, "La contraseña encontrada no es correcta."

def test_find_password_not_found():
    coded_password = hashlib.sha256("password123".encode("utf-8")).hexdigest()

    # Usar una lista de contraseñas que no contiene la contraseña buscada
    def read_passwords_not_found():
        return ["123456", "qwerty", "abc123"]

    found_password = find_password(coded_password, read_passwords_not_found)

    assert found_password is None, "La contraseña debería ser None si no se encuentra."

if __name__ == "__main__":
    pytest.main()
