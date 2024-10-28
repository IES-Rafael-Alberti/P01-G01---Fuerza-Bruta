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

## Herramientas

__Uso de la Biblioteca Hashlib__

1.- Introducción

En ciberseguridad, los ataques basados en contraseñas, como los de fuerza bruta y diccionario, son comunes y requieren algoritmos de hashing para comparar contraseñas de forma segura. Este proyecto utiliza la biblioteca Hashlib de Python para implementar estos ataques, y el informe detalla su funcionamiento, características y compara Hashlib con otras bibliotecas de hashing alternativas para ciberseguridad.

2.- Descripción de Hashlib

Hashlib es una biblioteca estándar de Python que ofrece implementaciones de algoritmos de hashing criptográfico populares, como MD5, SHA-1 y SHA-256. Su facilidad de uso y acceso a algoritmos estándar la hacen ideal para proyectos de hashing y ciberseguridad. Además, al estar integrada en Python, es eficiente y fácil de implementar en aplicaciones sin requerir dependencias externas.

3.- Características clave de Hashlib

- Compatibilidad y estándar de seguridad: Utiliza algoritmos que siguen estándares reconocidos como SHA-2 y SHA-3, asegurando la integridad de los datos.  
- Implementación sencilla: Ofrece una sintaxis directa, facilitando la generación de hashes.  
- Desempeño: Está optimizada para un rendimiento sólido, crucial en aplicaciones donde la velocidad de hashing es importante, como en ataques de fuerza bruta.  
- Limitaciones: No cuenta con soporte para algoritmos modernos de derivación de claves, como Argon2 o PBKDF2, lo que puede ser una desventaja para el almacenamiento seguro de contraseñas.

4.- Comparación de Hashlib con otras Bibliotecas de Hashing

A continuación, se presenta una comparación de Hashlib con otras librerías de hashing disponibles en Python que también podrían utilizarse en un contexto de ciberseguridad.

| Librería  | Algoritmos Soportados | Características Notables | Comparación con Hashlib |
| ----- | ----- | ----- | ----- |
| Bcrypt | BCrypt | Específicamente diseñado para hashing seguro de contraseñas | Mejor en hashing de contraseñas pero menos versátil |
| Passlib | BCrypt, PBKDF2, Argon2, SHA-512 | Ideal para almacenamiento seguro de contraseñas; usa “salting” automático | Más robusta para derivación de contraseñas, pero menos eficiente en hash simples |
| Pycryptodome | MD5, SHA-1, SHA-2, SHA-3, HMAC | Amplia variedad de algoritmos, incluye cifrado y soporte para HMAC | Orientada a aplicaciones de seguridad integrales, más pesada en recursos |
| Cryptography | SHA-1, SHA-256, SHA-512, Argon2 | Biblioteca versátil para criptografía completa, incluye cifrado de alto nivel y manejo de certificados | Potente pero puede ser excesiva para hashing directo |

5.- Recomendaciones

Se recomienda usar Hashlib para proyectos enfocados en ataques de fuerza bruta o diccionario, ya que permite una generación y comparación rápida de hashes. Sin embargo, para el almacenamiento seguro de contraseñas, es mejor optar por librerías como Passlib o bcrypt, que proporcionan una mayor protección mediante algoritmos de derivación de contraseñas y la técnica de "salting".


6.- Conclusión

Hashlib es una solución confiable y eficiente para realizar ataques de contraseña en entornos controlados y educativos, donde la velocidad de hashing es crucial. Para este proyecto, Hashlib es adecuado para simular ataques de diccionario o fuerza bruta, pero a largo plazo se sugiere evaluar librerías especializadas para el almacenamiento seguro de credenciales.

<br>

__Uso del diccionario SecLists__

1.- Introducción

En ciberseguridad, los diccionarios de contraseñas y nombres de usuario son esenciales para realizar pruebas de penetración y evaluar la seguridad de sistemas frente a ataques como los de diccionario y fuerza bruta. Este informe detalla las características de SecLists, su utilidad en ataques por diccionario y su comparación con otros diccionarios populares.

2.- Descripción de SecList

SecLists es un repositorio público de listas de palabras orientadas a ciberseguridad, disponible en GitHub y mantenido por la comunidad de seguridad, destacando figuras como Daniel Miessler y Jason Haddix. Esta colección incluye archivos de texto con listas optimizadas para diferentes pruebas de seguridad y ataques. Contiene amplias listas de contraseñas comunes, extraídas de filtraciones de datos, así como nombres de usuario frecuentes y sus variantes utilizadas en diversos servicios. También incluye payloads predefinidos para pruebas de vulnerabilidades, como inyecciones SQL y XSS, además de datos sobre subdominios y DNS que son útiles para el reconocimiento y el descubrimiento de subdominios. A su vez, SecLists abarca otras listas que contienen archivos y directorios comunes, extensiones de archivo, y datos relevantes para escaneo de redes y ataques de enumeración.

3.- Características clave de SecLists

- Actualización y mantenimiento constante: El repositorio de SecLists es actualizado regularmente, lo que permite contar con listas actualizadas que reflejan las tendencias y patrones actuales de ataques.  
- Cobertura de múltiples vectores de ataque: Al incluir no solo contraseñas y nombres de usuario, sino también payloads para inyección y escaneo, SecLists se convierte en una herramienta integral para pruebas de seguridad.  
- Compatibilidad con herramientas de ciberseguridad: La mayoría de herramientas populares como Burp Suite, OWASP ZAP, y Nmap, son compatibles con los archivos de SecLists y permiten su integración directa en las pruebas.  
- Disponibilidad gratuita y de fácil acceso: Al estar alojado en GitHub, SecLists es de acceso gratuito, lo que facilita su obtención e implementación en diversos entornos de seguridad.


4.- Comparación con Otros Diccionarios de Seguridad

La siguiente tabla compara SecLists con otros diccionarios de contraseñas y listas de ciberseguridad utilizados comúnmente:

| Diccionario | Contenido Principal | Características Destacadas | Comparación con SecLists |
| ----- | ----- | ----- | ----- |
| SecLists | Contraseñas, usuarios, payloads, subdominios | Actualización constante, muy completo, específico para ciberseguridad | Ofrece mayor variedad de listas para diferentes tipos de ataque |
| RockYou.txt	 | Contraseñas | Contiene millones de contraseñas filtradas de datos reales | Popular para ataques de fuerza bruta, pero no ofrece otros tipos de listas |
| Weakpass | Contraseñas | Base de datos en expansión de contraseñas comunes | Gran cantidad de contraseñas, pero sin payloads ni listas de usuarios |
| FuzzDB | Payloads de inyección, archivos, directorios | Repositorio para fuzzing y explotación | Enfocado en payloads y fuzzing, menos completo en contraseñas y usuarios |

6.- Conclusión

SecLists es una colección completa de listas para pruebas de seguridad, muy valorada en la comunidad de ciberseguridad por su constante actualización y versatilidad. Su uso en proyectos de pruebas de seguridad permite abordar diversos vectores de ataque, incluyendo fuerza bruta, inyección y descubrimiento de recursos en la red. Para ataques específicos, como la recuperación de contraseñas, SecLists ofrece listas amplias y actualizadas que aumentan las probabilidades de éxito en comparación con diccionarios más limitados. Por estas razones, SecLists es recomendado como un recurso esencial para este tipo de proyectos, ya que proporciona una variedad de listas útiles para pruebas de contraseñas, payloads de inyección y otros aspectos de seguridad, contribuyendo a una evaluación integral de vulnerabilidades.
### Resultados de las pruebas

### Resultados de las pruebas

### Resultados de las pruebas

