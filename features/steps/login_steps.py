from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'o usuario esteja na pagina de login')
def step_impl(context):
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/')
    
@when(u'o usuario entra com e-mail e senha válidos')
def step_impl(context):
    context.browser.find_element(By.ID, "mui-1").send_keys("alveslimaandre@gmail.com")
    context.browser.find_element(By.ID, "outlined-adornment-password").send_keys("senha1234")

@when(u'clica no botao de login')
def step_impl(context):
    context.browser.find_element(By.XPATH, "/html/body/div/main/form/button").click()

@then(u'o usuario deve ser redirecionado ao seu dashboard')
def step_impl(context):
    notification = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'go3958317564')))
    assert notification is not None, 'Notificação de login não encontrada'