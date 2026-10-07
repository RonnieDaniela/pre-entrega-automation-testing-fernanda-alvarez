# Automation Framework - SauceDemo E2E Tests

## Propósito del Proyecto
## El propósito de esta automatización es garantizar la calidad e integridad funcional de los componentes principales de la aplicación web SauceDemo. Las pruebas cubren escenarios clave como:
## Autenticación: Validación de inicio de sesión con credenciales válidas.
## Navegación e Interfaz: Verificación de títulos, presencia de elementos del menú, filtros y visibilidad del catálogo de productos.
## Gestión del Carrito: Selección de productos específicos, actualización dinámica del botón de estado (de Add to cart y Remove), contador del carrito y verificación de items dentro del carrito.
## Flujo de Checkout Completo: Navegación al checkout, carga de datos del formulario con datos personales, confirmación del resumen del pedido y validación del mensaje final de compra exitosa ("Thank you for your order!").

### Tecnologías Utilizadas
### Python 3.14.7: Lenguaje de programación principal.
### Pytest: Framework de pruebas para estructurar, gestionar las ejecuciones y manejar fixtures.
### Selenium WebDriver: Librería para la automatización e interacción con el navegador web.
### WebDriver Manager: Herramienta para la gestión y descarga automática del ejecutable del navegador (ChromeDriver).

#### Instalación de Dependencias
#### Para ejecutar los siguientes comandos por consola, abrir una terminal en la ruta raíz del proyecto
#### Requisitos Previos: Tener instalado Python 3.8+ instalado en el sistema. Se puede comprobar ejecutando: python --version
#### Para poder activar el entorno en Windows (PowerShell), ejecutar el comanto: python -m venv venv .\venv\Scripts\activate

##### Instalación de Paquetes
##### Instalacion de  los paquetes necesarios para los test utilizando `pip`: pip install pytest selenium webdriver-manager
##### Instalacion de los paquetes necesarios para los reportes: pip install pytest-html

###### Cómo Ejecutar las Pruebas
###### Abrir una terminal en la ruta raíz donde se encuentra el archivo test_saucedemo.py.
###### Utiliza los siguientes comandos: ppytest test_saucedemo.py
###### Para ver el detalle de cada prueba ejecutada y su resultado: pytest -v test_saucedemo.py
###### Para ejecutar las pruebas, ver el detalle de la ejecucion y generar el reporte HTML ejecutar el comando: pytest -v --html=reporte.html