import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    yield driver 

    driver.quit()



def test_01_login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    assert "/inventory.html" in driver.current_url , "ERROR: No se redirigió a /inventory.html"



def test_02_verificar_inventario( driver ):
    # driver.get("https://www.saucedemo.com/")

    # driver.find_element(By.ID, "user-name").send_keys("standard_user")
    # driver.find_element(By.ID, "password").send_keys("secret_sauce")
    # driver.find_element(By.ID, "login-button").click()

    page_title = driver.title
    section_title = driver.find_element(By.CLASS_NAME, "title").text

    assert page_title == "Swag Labs" , f'ERROR: Titulo de ventana esperado "swag labs", Obtenido {page_title}'

    assert section_title == 'Products' , f'ERROR: Titulo de seccion esperado "products", Obtenido {section_title}'


def test_03_productos_visibles(driver):

    inventory_item = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    # [] len() => ver que tan largo es una lista
    assert len(inventory_item) > 0 , f'ERROR: No se encontraron productos visibles'
    

def test_04_validad_interfaz( driver ):
    menu_button = driver.find_element(By.ID, 'react-burger-menu-btn')
    filtro = driver.find_element(By.CLASS_NAME, 'product_sort_container')


    assert menu_button.is_displayed(), f'ERROR: Menu no esta visible'
    assert filtro.is_displayed(), f'ERROR: filtro no esta visible'


def test_05a_añadir_primer_producto_al_carrito(driver):
    # 1. Agregar Remera Roja por su ID
    boton_tshirt = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    boton_tshirt.click()

    # Validar que el botón cambió a "Remove"
    boton_tshirt_actualizado = driver.find_element(By.ID, "remove-test.allthethings()-t-shirt-(red)")
    assert boton_tshirt_actualizado.text.capitalize() == 'Remove', 'ERROR: El botón de la remera roja no cambió a "Remove"'


def test_05b_añadir_segundo_producto_al_carrito(driver):
    # 2. Agregar Campera por su ID
    boton_jacket = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    boton_jacket.click()

    # Validar que el botón cambió a "Remove"
    boton_jacket_actualizado = driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket")
    assert boton_jacket_actualizado.text.capitalize() == 'Remove', 'ERROR: El botón de la campera no cambió a "Remove"'

def test_06_verificar_contador_carrito( driver ):
    contador_carrito = driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text

    assert contador_carrito == "2" ,f'ERROR: Se esperaba 2 , obtuvo {contador_carrito}'


def test_07_navegar_carrito(driver):
    # Espera a que el botón del carrito sea clickeable antes de presionar
    boton_carrito = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link')))
    boton_carrito.click()
    
    # Espera la confirmación de la nueva URL
    WebDriverWait(driver, 16).until(EC.url_contains("/cart.html"))
    assert "/cart.html" in driver.current_url, "ERROR: No se redirigió a /cart.html"

def test_08_comprobar_poducto_en_el_carrito(driver):
    # Obtenemos los nombres de todos los productos en el carrito
    elementos_carrito = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    nombres_en_carrito = [item.text for item in elementos_carrito]

    # Reemplazamos 'Sauce Labs Backpack' por 'Test.allTheThings() T-Shirt (Red)'
    assert 'Test.allTheThings() T-Shirt (Red)' in nombres_en_carrito, 'ERROR: "Test.allTheThings() T-Shirt (Red)" no está en el carrito'
    assert 'Sauce Labs Fleece Jacket' in nombres_en_carrito, 'ERROR: "Sauce Labs Fleece Jacket" no está en el carrito'

def test_09_iniciar_checkout(driver):
    # Esperar a que el botón Checkout sea clickeable antes de presionar
    boton_checkout = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "checkout")))
    boton_checkout.click()

    # Esperar la redirección a checkout-step-one.html
    WebDriverWait(driver, 16).until(EC.url_contains("/checkout-step-one.html"))
    assert "/checkout-step-one.html" in driver.current_url, "ERROR: No se redirigió a /checkout-step-one.html"


def test_10_completar_formulario_checkout(driver):
    # Completa los campos de información personal
    driver.find_element(By.ID, "first-name").send_keys("Ronnie")
    driver.find_element(By.ID, "last-name").send_keys("Daniela")
    driver.find_element(By.ID, "postal-code").send_keys("7111")

    # Hace clic en el botón 'Continue'
    driver.find_element(By.ID, "continue").click()

    # Espera a redirigir al resumen del pedido (Paso 2)
    WebDriverWait(driver, 16).until(EC.url_contains("/checkout-step-two.html"))
    assert "/checkout-step-two.html" in driver.current_url, "ERROR: No se redirigió a /checkout-step-two.html"


def test_11_finalizar_compra(driver):
    # Hace clic en el botón 'Finish' para procesar la compra
    driver.find_element(By.ID, "finish").click()

    # Espera a la pantalla final de confirmación
    WebDriverWait(driver, 16).until(EC.url_contains("/checkout-complete.html"))
    assert "/checkout-complete.html" in driver.current_url, "ERROR: No se redirigió a /checkout-complete.html"

    # Valida el mensaje de agradecimiento
    mensaje_exito = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert mensaje_exito == "Thank you for your order!", f'ERROR: Mensaje esperado "Thank you for your order!", Obtenido "{mensaje_exito}"'