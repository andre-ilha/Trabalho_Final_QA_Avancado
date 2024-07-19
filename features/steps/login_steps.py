from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given(u'o usuario esteja na pagina de login')
def step_impl(context):
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/')
    

@when(u'o usuario entra com e-mail e senha válidos')
def step_impl(context):
    context.browser.find_element(By.ID, "email").send_keys("user@example.com")
    context.browser.find_element(By.ID, "password").send_keys("password" + Keys.RETURN)

@when(u'clica no botao de login')
def step_impl(context):
    assert "Joga Junto" in context.browser.title


@then(u'o usuario deve ser redirecionado ao seu dashboard')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o usuario deve ser redirecionado ao seu dashboard')