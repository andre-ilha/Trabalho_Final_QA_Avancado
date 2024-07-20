from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given(u'o usuário estaja na página da lista de produtos')
def step_impl(context):
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/')
    context.browser.find_element(By.ID, "mui-1").send_keys("alveslimaandre@gmail.com")
    context.browser.find_element(By.ID, "outlined-adornment-password").send_keys("senha1234" + Keys.ENTER)
    assert "Joga Junto" in context.browser.title, 'Usuário não logado'

@when(u'o usuário digita o produto procurado na barra de busca')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/header/section[2]/nav/ul/div[1]/input"))
    ).send_keys("Beleza pura")


@then(u'o produto deve ser mostrado no resultado da busca')
def step_impl(context):
    WebDriverWait(context.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Beleza pura')]"))
    )
    assert "Beleza pura" in context.browser.page_source