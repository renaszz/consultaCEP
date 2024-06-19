import requests

def consultar_endereco(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

def main():
    cep = input("Digite o CEP: ")

    endereco = consultar_endereco(cep)

    if endereco:
        print("Resultado da consulta:")
        print(f"Rua: {endereco['logradouro']}")
        print(f"Bairro: {endereco['bairro']}")
        print(f"Cidade: {endereco['localidade']}")
        print(f"Estado: {endereco['uf']}")
    else:
        print(f"CEP não encontrado.")

if __name__ == '__main__':
    main()
