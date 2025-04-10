pergunta = """
Olá, tudo bem?
O que você deseja da lista abaixo?
(1) laranja
(2) cerveja 
(3) miojo
(4) carvão
(5) picanha
"""

opcao = input(pergunta)

agradecimento = "Obrigado pela preferência!"

if opcao == "1":
    print("Aqui está sua laranja!")
    print(agradecimento)
elif opcao == "2":
    print("Aqui está sua cerveja!")
    print(agradecimento)
elif opcao == "3":
    print("Aqui está seu miojo!")
    print(agradecimento)
elif opcao == "4":
    print("Aqui está seu carvão!")
    print(agradecimento)
elif opcao == "5":
    print("Aqui está sua picanha!")
    print(agradecimento)
else:
    print("Não temos esse produto!")

# %%

pergunta = """
Olá, tudo bem?
O que você deseja?
"""

opcao = input(pergunta)

agradecimento = "Obrigado pela preferência!"

if opcao in ["laranja", "cerveja", "miojo", "carvão", "picanha"]:
    print("Aqui está o seu produto!")
    print(agradecimento)
else:
    print("Não temos o produto", opcao)
