#%%
dic_contatos = {}

while True:
    nome = input("Qual seu nome: ")
    if nome == "":
        break
    else:
        telefone = input("Qual seu número de telefone: ")
        dic_contatos[nome] = telefone

while True:
    busca = input("Digite um nome para buscar o telefone (ou pressione Enter para sair): ")
    if busca == "":
        break
    elif busca in dic_contatos:
        print(f"Telefone de {busca}: {dic_contatos[busca]}")
    else:
        print(f"{busca} não está na lista de contatos.")

for nome, telefone in dic_contatos.items():
    print((f"{nome} : {telefone}"))