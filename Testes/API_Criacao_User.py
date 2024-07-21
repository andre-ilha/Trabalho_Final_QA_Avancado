import json
import requests
from faker import Faker
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

fake = Faker('pt_br')

def salvar_json(logjson: str, conteudo: str):
    with open(logjson, 'w') as arquivo:
        arquivo.write(conteudo + '\n')
    print(f'Dados salvos em {logjson}.')

def create_user_api():
    endpoint_new_user = 'https://apipf.jogajuntoinstituto.org/register'
    register_data = {
        'email': fake.email(),
        'password': fake.password()
    }

    response = requests.post(endpoint_new_user, json=register_data)

    if response.status_code == 200:
        print('Criação de usuário realizado com sucesso!')
        response_data = response.json()
        print(response_data)
        salvar_json('resposta_novo_user.json', json.dumps(response_data, indent=4))
        return register_data
        
    else:
        print('Falha ao criar usuário.')
        print('Status code:', response.status_code)
        print('Resposta:', response.json())
        salvar_json('resposta_novo_user.json', json.dumps(response.json(), indent=4))
        return None

def login_user_api(email, password):
    endpoint_login = 'https://apipf.jogajuntoinstituto.org/login'
    login_data = {
        'email': email,
        'password': password
    }

    response = requests.post(endpoint_login, json=login_data)

    if response.status_code == 200:
        print('Login realizado com sucesso!')
        response_data = response.json()
        print(response_data)
        print(login_data)
        salvar_json('resposta_login.json', json.dumps(response_data, indent=4))
        return response_data.get('token')
    else:
        print('Falha ao realizar login.')
        print('Status code:', response.status_code)
        print('Resposta:', response.json())
        salvar_json('resposta_login.json', json.dumps(response.json(), indent=4))
        return None
    
def criar_produto(token):
    endpoint_criar_produto = 'https://apipf.jogajuntoinstituto.org/'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    produto_data = {
        "name": "Tatuagem BarberShop",
        "description": "Tatuagem provisório de um barbudo style, para você ficar mais elegante",
        "price": "10,90",
        "category": "Acessorios",
        "shipment": "4,00",
        "image": "C:\\Users\\andre\\OneDrive\\Imagens\\tattoo2.jpg"
    }

    files = {
        'image': open(produto_data['image'], 'rb')
    }
    
    response = requests.post(endpoint_criar_produto, headers=headers, data=produto_data, files=files)

    if response.status_code == 200:
        print('Produto criado com sucesso!')
        response_data = response.json()
        print(response_data)
        salvar_json('resposta_criar_produto.json', json.dumps(response_data, indent=4))
        return response_data  # Retorna o response_data completo, que inclui o ID do produto
    else:
        print('Falha ao criar produto.')
        print('Status code:', response.status_code)
        print('Resposta:', response.json())
        salvar_json('resposta_criar_produto.json', json.dumps(response.json(), indent=4))
        return None

def dados_user_api(token):
    endpoint_dados = 'https://apipf.jogajuntoinstituto.org/'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    response = requests.get(endpoint_dados, headers=headers)

    if response.status_code == 200:
        print('Dados requisitados com sucesso!')
        response_data = response.json()
        df = pd.DataFrame(response_data)
        print(df)
        salvar_json('resposta_lista_prod.json', json.dumps(response_data, indent=4))
        return df
    else:
        print('Falha ao requisitar dados.')
        print('Status code:', response.status_code)
        print('Resposta:', response.json())
        salvar_json('resposta_lista_prod.json', json.dumps(response.json(), indent=4))
        return None

def abrir_navegador(email, password):
    browser = Firefox()
    link = 'https://projetofinal.jogajuntoinstituto.org/'
    browser.get(link)
    browser.find_element(By.ID, "mui-1").send_keys(email)
    browser.find_element(By.ID, "outlined-adornment-password").send_keys(password + Keys.ENTER)
    time.sleep(10)
    browser.quit()

def deletar_produto(token, produto_id):
    endpoint_deletar_produto = f'https://apipf.jogajuntoinstituto.org/{produto_id}'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.delete(endpoint_deletar_produto, headers=headers)

    if response.status_code == 200:
        print('Produto deletado com sucesso!')
        salvar_json('resposta_deletar_produto.json', json.dumps(response.json(), indent=4))
    else:
        print('Falha ao deletar produto.')
        print('Status code:', response.status_code)
        print('Resposta:', response.json())
        salvar_json('resposta_deletar_produto.json', json.dumps(response.json(), indent=4))

user_data = create_user_api()

if user_data:
    token = login_user_api(user_data['email'], user_data['password'])
    
    if token:
        produto_response = criar_produto(token)
        if produto_response:
            dados_user_df = dados_user_api(token)
            abrir_navegador(user_data['email'], user_data['password'])
            
            # Extraindo o ID do produto do DataFrame
            produto_id = dados_user_df['idprodutos'].iloc[0] if not dados_user_df.empty else None
            
            del_arquivo = input('Você gostaria de deletar o produto criado? Digite S [Sim] ou N [Não]').lowers()
            if del_arquivo == 's':
                if produto_id:
                    deletar_produto(token, produto_id)
                else:
                    print('ID do produto não encontrado.')