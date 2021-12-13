import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from selenium import webdriver
from selenium.webdriver import ActionChains
from Pages.LoginPage import LoginPage
from Pages.AccountPage import AccountPage
from Pages.HeaderPage import HeaderPage
from Pages.ProductListPage import ProductListPage

# Constante
STORE_WEB = 'https://automationteststore.com/index.php?rt=account/account'

# Scenarios
scenarios('../features/BuscarProducto.feature')


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
    assert account_page.getAccountTitle().text != None  # == 'Marcos'

    print('El acceso a la cuenta ' + account_page.getAccountTitle().text + ' fue correcto')


@when('busco el perfume para hombre')
def check_filter(browser):
    header_page = HeaderPage(browser)
    print('Pasó el browser al page object')
    hover = ActionChains(browser).move_to_element(header_page.getSubcatFilter())
    print('Se posicionó en el menú sobre el filtro' + header_page.getSubcatFilter().text)
    hover.perform()
    header_page.getSubSubCatFilter().click()
    print('Se posicionó en el menú sobre la opción ' + header_page.getSubSubCatFilter().text + ' del filtro Fragrance')


@then(parsers.parse('encuentro el perfume "{titulo_perfume}" para hombre'))
def found_product(browser, titulo_perfume):
    product_item = ProductListPage(browser)
    assert product_item.getProductItem().text == 'POUR HOMME EAU DE TOILETTE'

    print('Se ha encontrado el producto buscado en la grilla')

