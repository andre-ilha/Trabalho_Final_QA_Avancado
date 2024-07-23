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
    notification = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'go3958317564')))
    assert notification is not None, 'Notificação de login não encontrada'
    time.sleep(10)
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/header/section[2]/div/header/button'))).click()
    time.sleep(2)

@when(u'o usuario entra com dados válidos do produto')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/header/section[2]/div/div[1]/div/form/div[3]/div/label[3]/span'))).click()
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.ID, 'mui-5'))).send_keys(r'C:\Users\andre\OneDrive\Imagens\tattoo2.jpg')
    context.browser.find_element(By.ID, 'mui-2').send_keys('Tatuagem BarberShop')#Nome
    context.browser.find_element(By.ID, 'mui-3').send_keys('Tatuagem provisório de um barbudo style, para você ficar mais elegante')#Descrição
    context.browser.find_element(By.ID, 'mui-4').send_keys('10,90')#Preço
    context.browser.find_element(By.ID, 'mui-6').send_keys('4,90')#Frete
    time.sleep(5)

@when(u'clica no botao de ENVIAR NOVO PRODUTO')
def step_impl(context):
    context.browser.find_element(By.XPATH, '/html/body/div/header/section[2]/div/div[1]/div/form/button').click()

@then(u'uma confirmacao deve retornar ao usuário')
def step_impl(context):
    notification = WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'go3958317564')))
    assert notification is not None, 'Notificação de login não encontrada'

@then(u'o produto deve ser adicionado a lista de produtos')
def step_impl(context):
    body_element = context.browser.find_element(By.ID, 'mui-2')
    body_element.send_keys(Keys.ESCAPE)
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/header/section[2]/nav/ul/div[1]/input"))).send_keys("Tatuagem BarberShop")
    WebDriverWait(context.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Tatuagem BarberShop')]")))
    assert "Tatuagem BarberShop" in context.browser.page_source
    time.sleep(10)