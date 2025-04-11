# %%

# Uma maneira de difinir listas

idades = [28, 42, 43, 35, 39, 28, 22]

print(idades)

# %%

joao = ["João", "Fernandes", 23, False, "Namorando", 4030.03]

print(joao)

# Tipo
print(type(joao))

# Idade
print(joao[2])

# Renda
print(joao[5])

# Nome
print(joao[0])

# %%

idades = [28, 42, 43, 35, 39, 15, 22, 50]

# sum vai somar os valor da lista
soma_idades = sum(idades)

# len vai dizer o tamnho da lista
qtde_idades = len(idades)

print("Soma das idades:", soma_idades)

print("Qtde idades:", qtde_idades)

print("Media das idades:", int(soma_idades/qtde_idades))

print("Menor idade:", min(idades))

print("Meior idade:", max(idades))

# %%

joao = ["João Fernandes", 
        23, 
        False, 
        "Namorando",
        ["Op. monitoramento", "P.A", "Analista op.", "Anaista QA", "Analista Dados"],
        [1500, 1800, 2400, 2600, 6500],
        ["J", "R", "P"]]

print("Tamanho da lista:", len(joao))

# Primera forma de ler a informação de uma lista 
# dentro de uma lista
print(joao[6][0])

# Segunda forma de ler a informação de uma lista
# dentro de uma lista
letra = joao[6]
primeira_letra = letra[0]
print(primeira_letra)

# Ter acesso as quantidades de itens, e acessar o item na posição correta

tamanho = len(joao)
pos = tamanho -1
letras = joao[pos]

joao[pos][len(letras)-1]

# Para acessar o ultimo elementos da lista é só utilizar o -1

print(joao[-1][-1])

# Pegar os dois ultimos elementos da sub lista
print(joao[4][3:5])

# Pegar os dois ultimos elementos da sub lista
print(joao[4][-2:])

# Primeiros 3 elementos
print(joao[4][:3])

# joao[ start : stop]

salarios = joao[5]
salarios[::-1]

# joao[ start : stop : step ]

# Pegar elementos de 2 em 2
joao[5][::2]