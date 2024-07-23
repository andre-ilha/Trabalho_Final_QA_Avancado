from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker

fake = Faker()
email = fake.email()
password = fake.password()

@given(u'o usuario esteja na página de registro')
def step_impl(context):
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/')
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/form/div[6]/span[2]/a'))).click()
    time.sleep(3)

@when(u'ele preenche os dados com informações válidas')
def step_impl(context):
    context.browser.find_element(By.XPATH, '//*[@id="mui-2"]').send_keys(email)
    context.browser.find_element(By.XPATH, '//*[@id="outlined-adornment-password"]').send_keys(password)
    context.browser.find_element(By.XPATH, '/html/body/div/div/form/div/div[3]/div/div[1]/input').send_keys(password)
    
@when(u'clica em criar conta')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/form/button'))).click()


@then(u'uma confirmacao deve retornar ao usuario e retorna a página principal para login')
def step_impl(context):
    success_message = WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Usuário cadastrado com sucesso')]"))
    )
    assert success_message is not None
    time.sleep(5)
    assert "Joga Junto" in context.browser.title
