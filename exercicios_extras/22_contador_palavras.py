#%%
def cont_palavras():
    dic_palavras = {}
    while True:
        palavras = input("Informe uma palavra (ou pressione Enter para sair): ")
        if palavras == "":
            break

        if palavras not in dic_palavras:
            dic_palavras[palavras] = 1
        else:
            dic_palavras[palavras] += 1

    for palavra, contagem in dic_palavras.items():
        print(palavra, "=", contagem)

cont_palavras()