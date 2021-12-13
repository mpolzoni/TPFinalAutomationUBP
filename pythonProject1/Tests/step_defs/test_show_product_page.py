import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from selenium import webdriver
from selenium.webdriver import ActionChains
from Pages.LoginPage import LoginPage
from Pages.AccountPage import AccountPage
from Pages.HeaderPage import HeaderPage
from Pages.ProductListPage import ProductListPage
from Pages.ProductPage import ProductPage

#Constante
STORE_WEB = 'https://automationteststore.com/index.php?rt=account/account'

#Scenarios
scenarios('../features/MostrarPaginaProducto.feature')

@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.maximize_window()
    b.implicitly_wait(15)
    yield b
    b.quit()

@given('la pagina de venta')
def open_store_web(browser):
    browser.get(STORE_WEB)
    print('Abre la página')

@when(parsers.parse('se completa el "{username}" y "{password}"'))
def complete_user_pass(browser, username, password):
    login_page = LoginPage(browser)
    print('Pasa el browser')

    login_page.getUserInput().send_keys(username)
    print('Envia el username')

    login_page.getPassInput().send_keys(password)
    print('Envia el password')

    login_page.getLoginBtn().click()
    print('Click sobre el boton Login')

@when('mi cuenta de usuario se muestra en pantalla')
def check_title(browser):
    account_page = AccountPage(browser)
    assert account_page.getAccountTitle().text != None #== 'Marcos'

    print('El acceso a la cuenta ' + account_page.getAccountTitle().text + ' fue correcto')

@when('busco el perfume para hombre')
def check_filter(browser):
    header_page = HeaderPage(browser)
    print('Pasó el browser al page object')
    hover = ActionChains(browser).move_to_element(header_page.getSubcatFilter())
    print('Se posicionó en el menú sobre el filtro'+ header_page.getSubcatFilter().text)
    hover.perform()
    header_page.getSubSubCatFilter().click()
    print('Se posicionó en el menú sobre la opción '+header_page.getSubSubCatFilter().text+' del filtro'+ header_page.getSubcatFilter().text)

@when('selecciono un producto')
def select_product(browser):
    print('Llega acá')
    product_item = ProductListPage(browser)
    print('Pasó el browser')
    product_item.getProductItem().click()
    print('Se seleccionó el perfume')


@then(parsers.parse('encuentro el perfume "{titulo_perfume}" para hombre'))
def found_product(browser, titulo_perfume):
    product_item = ProductListPage(browser)
    assert product_item.getProductItem().text == 'POUR HOMME EAU DE TOILETTE'
    print('Se ha encontrado el producto buscado en la grilla')

@then('se muestra la pagina del producto')
def show_product(browser):
    product_page = ProductPage(browser)
    assert product_page.getProductName().text == 'Pour Homme Eau de Toilette'
    print('Se muestra el titulo del producto ' + product_page.getProductName().text +' correctamente.')

    #me aseguro posicionarme sobre solapa descripción y le hago clic
    product_page.getFlapDescription().click()
    print('Se posicionó sobre la solapa ' + product_page.getFlapDescription().text)

    #comparo la descripción del producto con la descripción esperada
    assert product_page.getDescription().text == 'An intriguing masculine fragrance that fuses the bracing freshness of Darjeeling tea with the intensity of spice and musk. For those seeking a discreet accent to their personality.'
    print('La descripción del producto es la correcta')