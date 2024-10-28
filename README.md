# Proyecto: Script de Fuerza Bruta con SHA y Diccionario

## Descripción
Este proyecto tiene como objetivo desarrollar un script en Python que permita comprobar, mediante fuerza bruta y utilizando un diccionario, el texto con el cual se generó un valor hash mediante el algoritmo SHA (en este caso, SHA-256). Este script puede ser útil en prácticas de ciberseguridad y criptografía, donde se busca recuperar texto original de hashes.

## Estructura de Roles del Equipo
El proyecto se organiza en torno a cinco roles clave:

1. **Product Owner**: Organiza las tareas, asegura el cumplimiento del calendario, y mantiene la estructura de trabajo.
2. **Technical Chief**: Investiga las tecnologías y algoritmos necesarios.
3. **Q&A (Quality Assurance)**: Desarrolla y supervisa las pruebas del código.
4. **DevOps**: Configura la automatización de pruebas de código con GitHub Actions.
5. **Developer**: Desarrolla el código del script y documenta su funcionamiento.

## Características Principales
- **Lenguaje**: Python
- **Algoritmo de Hash**: SHA-256
- **Automatización**: GitHub Actions para CI/CD
- **Pruebas**: Utilización de pytest para asegurar la calidad del código

## Requerimientos
Para ejecutar el script, asegúrate de tener:
- **Python** 3.6 o superior.
- Biblioteca `hashlib` (viene por defecto en Python).
- Biblioteca `pytest` para ejecutar las pruebas unitarias. 
