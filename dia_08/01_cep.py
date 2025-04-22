# %%
import requests # para realizar requisições na web
import json # para tratar json de listas/dicionarios para arquivos json

ceps = [
    "89700053",
    "90810240",
    "20531540",
    "88000000",
    "89636000",
    "89830000",
]

#%%

url = "https://cep.awesomeapi.com.br/json/{cep}"
dados = []
for i in ceps:
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados
#%%
print(dados)

with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)