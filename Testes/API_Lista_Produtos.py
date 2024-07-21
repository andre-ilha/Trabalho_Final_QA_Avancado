import json
import requests
import pandas as pd

def salvar_json(logjson: str, conteudo: str):
    with open(logjson, 'w') as arquivo:
        arquivo.write(conteudo + '\n')
    print(f'Dados salvos em {logjson}.')

def login_user_api():
    endpoint_login = 'https://apipf.jogajuntoinstituto.org/login'
    login_data = {
        'email': "alveslimaandre@gmail.com",
        'password': "senha1234"
    }

    response = requests.post(endpoint_login, json=login_data)

    if response.status_code == 200:
        print('Login realizado com sucesso!')
        response_data = response.json()
        print(response_data)
        salvar_json('resposta_api.json', json.dumps(response_data, indent=4))
        return response_data.get('token')
    else:
        print('Falha ao realizar login.')
        print('Status code:', response.status_code)
        print('Resposta:', response.json())
        salvar_json('resposta_api.json', json.dumps(response.json(), indent=4))
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
        salvar_json('dados_api.json', json.dumps(response_data, indent=4))
    else:
        print('Falha ao requisitar dados.')
        print('Status code:', response.status_code)
        print('Resposta:', response.json())
        salvar_json('dados_api.json', json.dumps(response.json(), indent=4))

token = login_user_api()
if token:
    dados_user_api(token)
