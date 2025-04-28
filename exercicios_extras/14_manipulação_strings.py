#%%
nome = input("Inclua seu nome completo: ")
quantidade_letras = len(nome.replace(" ", ""))
primeiro_nome = nome.split()[0]

print(nome.upper())
print(quantidade_letras)
print(primeiro_nome.lower())