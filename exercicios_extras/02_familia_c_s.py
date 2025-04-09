pergunta = """
Qual a sua familia?
(1) Calvo
(2) Silva
(3) Outro
"""

opcao = input(pergunta)

if opcao == "1":
    print("Olá Sr. Calvo")
    exit()
elif opcao == "2":
    print("Olá Sr. Silva")
    exit()

outro = input("Qual o sobrenome da sua familia? ")

if opcao == "3":
    print("Olá Sr.", outro)
else:
    print("Essa opções não existe!")