# %%

lista = [2, 132, "joao", ["ds", "de", "da"], True]

lista[2]

# %%
# Dicionarios, são pares de chave/valor, chave associada a um valor

dados_joao = {
    "sobrenome":"Fernandes",
    "nome":"João", 
    "filhos":False,
    "formacao":["Fundamental", "Medio"],
    "cargos":[
        {"nome":"Analista QA", "empresa":"Raster"},
        {"nome":"Pré - Teste", "empresa":"Arpa"},
        {"nome":"Analista Dados jr", "empresa":"Coperdia"},
        {"nome":"Analista Dados", "empresa":"Fleury"}
    ]
}

print(dados_joao)

# Passar a chave para obter o valor da mesma
print(dados_joao["formacao"])
print(dados_joao["formacao"][-1])
print(dados_joao["cargos"])
print(dados_joao["cargos"][-1]["empresa"])

dados_joao["estado civil"] = "Namorando"

print(dados_joao)

# Usar keys para descobrir os nomes das chaves
print("Chaves:", dados_joao.keys())

# Usar values para descobrir os valores
print("Valores:", dados_joao.values())

# Usar items para trazer chaves/valores
print("Itens:", dados_joao.items())

# For percorendo um dicionario
for i in dados_joao:
    print(i, "=", dados_joao[i])

# Usando o items no for
for item in dados_joao.items():
    print(item)

# Usando o items no for e separando chave e valor
for chave, valor in dados_joao.items():
    print(chave, "=", valor)