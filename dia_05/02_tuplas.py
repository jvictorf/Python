# %%

dados_joao = [23, 1, "Namorando", "Analista de Dados Jr"]
print(dados_joao)

dados_joao.append("4000.34")
print(dados_joao)

# Duas formas de fazer uma tupla
# tupla_joao = 23, 1, "Namorando", "Analista de Dados Jr"
tupla_joao = (23, 1, "Namorando", "Analista de Dados Jr")
print(type(tupla_joao))
print(tupla_joao)

# Não é possivel alterar uma tupla com o append por exemplo 

# %%

tupla_joao = (23, 1, "Namorando", "Analista de Dados Jr", ["a", "b", "c"])
print(tupla_joao)
tupla_joao[-1].append("d")
print(tupla_joao)