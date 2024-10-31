import pytest
from hash_module import hashear, comprobarDict

#passwords_file = open("passwords.txt")

def test_hashear():
    assert hashear("Gonzalo") == "b52739680491747f171140e41b7235006ec442c7c5d4399d0a36c7c44988dda7"
    assert hashear("123456") == "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"

def test_comprobarDict():
    passwords_file = open("passwords.txt")
    # Test con: 123456
    assert comprobarDict("8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92", passwords_file) == True
    # Test con: password
    assert comprobarDict("5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8", passwords_file) == True
    # Test con: iloveyou
    assert comprobarDict("e4ad93ca07acb8d908a3aa41e920ea4f4ef4f26e7f86cf8291c5db289780a5ae", passwords_file) == True
    # Test con: grupo1
    assert comprobarDict("6b51e44c3e40760ac733e079052685dbcedfa77e8f1fff45848740858fec3b85", passwords_file) == False
    # Test con: Gonzalo
    assert comprobarDict("b52739680491747f171140e41b7235006ec442c7c5d4399d0a36c7c44988dda7", passwords_file) == False