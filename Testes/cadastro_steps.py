from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given(u'o usuario esteja na pagina de cadastro')
def step_impl(context):
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/')
    context.browser.find_element(By.ID, "mui-1").send_keys("alveslimaandre@gmail.com")
    context.browser.find_element(By.ID, "outlined-adornment-password").send_keys("senha1234" + Keys.ENTER)
    assert "Joga Junto" in context.browser.title, 'Usuário não logado'
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/header/section[2]/div/header/button'))).click()

@when(u'o usuario entra com dados válidos do produto')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/header/section[2]/div/div[1]/div/form/div[3]/div/label[1]'))).click()
    #WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mui-5"'))).click()
    context.browser.find.element(By.CSS_SELECTOR, '#mui-7').send_key('Camiseta Azul')#Nome
    context.browser.find.element(By.ID, 'mui-3').send_key('Camiseta bonita')#Descrição
    context.browser.find.element(By.ID, 'mui-4').send_key('59,90')#Preço
    context.browser.find.element(By.ID, 'mui-6').send_key('19,90')#Frete


# @when(u'clica no botao de ENVIAR NOVO PRODUTO')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When clica no botao de salvar')


# @then(u'o produto deve ser adicionado a lista de produtos')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then o produto deve ser adicionado a lista de produtos')


# @then(u'uma confirmacao deve retornar ao usuario')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then uma confirmacao deve retornar ao usuario')