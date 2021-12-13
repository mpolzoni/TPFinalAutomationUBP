import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.AccountPage import AccountPage

#Constante
STORE_WEB = 'https://automationteststore.com/index.php?rt=account/login'

#Scenarios
scenarios('../features/Login.feature')

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

@then('mi cuenta de usuario se muestra en pantalla')
def check_title(browser):
    account_page = AccountPage(browser)
    assert account_page.getAccountTitle().text == 'Marcos'
    print('El acceso a la cuenta ' + account_page.getAccountTitle().text + ' fue correcto')