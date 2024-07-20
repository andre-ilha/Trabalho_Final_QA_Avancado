from faker import Faker
import json
import requests

fake = Faker('pt_BR')

def criar_persona() -> dict:

    data = {
        "email" : fake.email(),
        "password" : fake.password()
        }
    return data

def salvar_json(logjson: str, conteudo: str):
    with open(logjson, 'w') as arquivo:
        arquivo.write(conteudo + '\n')
    print(f'Dados salvo em {logjson}.')

def criar_user_api() -> bool:
    endpoint_criaruser = "https://apipf.jogajuntoinstituto.org/api/register/"
    response = requests.post(endpoint_criaruser, json=usuario)

    if response.status_code == 201:
        print('Usuário criado com sucesso!')
        print(response.json())
        salvar_json('log_criacao.json', json.dumps(response.json(), indent=4))
        return True
    else:
        print('Falha ao criar usuário.')
        print('Status code: ', response.status_code)
        print('Resposta: ', response.json())
        salvar_json('log_criacao.json', json.dumps(response.json(), indent=4))
        return False

# def login_user_api():
#     endpoint_login = 'http://desafiopython.jogajuntoinstituto.org/api/users/login/'
#     login_data = {
#         'email': usuario["email"],
#         'password':usuario["password"]
#     }

#     response = requests.post(endpoint_login, json=login_data)

#     if response.status_code == 200:
#         print('Login realizado com sucesso!')
#         print(response.json())
#         salvar_json('reposta_api.json', json.dumps(response.json(), indent=4))
#     else:
#         print('Falha ao realizar login.')
#         print('Status code:', response.status_code)
#         print('Resposta:', response.json())
#         salvar_json('reposta_api.json', json.dumps(response.json(), indent=4))

usuario = criar_persona()
criar_user_api()
# if criar_user_api():
#      login_user_api()