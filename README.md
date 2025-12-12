**QA Automation Exercises (API + Web)**

Este repositorio contiene la solución de los Ejercicios Prácticos del examen para Ingeniero QA Semi-Senior.
Incluye:

🧪 Pruebas de API con Python + Requests

🌐 Automatización Web con Selenium + Pytest

🧱 Arquitectura Page Object Model (POM)

**🧪 Exercise 1 – API Testing (Pokémon API)**

✔ Endpoint validated
https://pokeapi.co/api/v2/pokemon/pikachu

✔ Requirements

1. Validar que el status code sea 200

2. Validar que "name" == "pikachu"

3. Implementar la solución usando Python + Requests

**Exercise 2 – Web Automation (Selenium + Pytest + POM)**

✔ Link para automatizar prueba
https://example.com/login

**🧱 Arquitectura Page Object Model (POM)**

Los archivos del módulo Web contienen:

data.py → valores de configuración (URL, usuario, contraseña)

locators.py → todos los selectores Selenium

methods.py → clase Page Object con todas las acciones

test_login.py → prueba automatizada con pytest

main.py → ejecución manual sin pytest

**🎯 Resultado**

Este repositorio demuestra:

✔ Pruebas de API estructuradas
✔ Automatización Web con Selenium + Pytest
✔ Implementación profesional de Page Object Model
✔ Selectores limpios y mantenibles
✔ Código preparado para entornos reales de QA