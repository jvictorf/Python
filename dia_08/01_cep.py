# %%
import requests # para realizar requisições na web
import json # para tratar json de listas/dicionarios para arquivos json
from tqdm import tqdm # load dos dados
import pandas as pd # pandas é usado para transformar esse dados

ceps = [
    "89700053",
    "90810240",
    "20531540",
    "88000000",
    "89636000",
    "89830000",
]

url = "https://cep.awesomeapi.com.br/json/{cep}"
dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)