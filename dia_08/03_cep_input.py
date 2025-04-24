#%%

import requests

cep = input("Entre com um CEP: ")

url = "https://cep.awesomeapi.com.br/json/{cep}"

resposta = requests.get(url.format(cep=cep))
if resposta.status_code == 200:
    dados = resposta.json()

function
for chave, valor in dados.items():
    print(chave, "->", valor)