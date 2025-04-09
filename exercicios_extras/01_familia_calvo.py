pergunta = """
Você é da família Calvo?
(1) Sim
(2) Não
"""

opcao = input(pergunta)

familia = "Calvo"

if opcao == "1":
    print("Olá Sr.", familia)
elif opcao == "2":
    print("Você não é dessa família!")
else:
    print("Essa opções não existe!")