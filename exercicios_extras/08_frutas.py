# Escreva um programa que crie um dicionário com nomes de frutas como 
# chaves e seus respectivos preços como valores.
# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

# %%

Frutas = {
    "Maça": "R$1.50",
    "Banana": "R$2.75",
    "Uva": "R$1.90",
    "Pera": "R$1.25",
    "Laranja": "R$0.65",
    "Limão": "R$1.25",
    "Goiaba": "R$2.15",
    "Abacaxi": "R$3.20",
    "Jaca": "R$5.80"
}

fruta = input("Digite o nome de uma fruta: ")

if fruta in Frutas:
    print("O valor da fruta", fruta, "é", Frutas[fruta])
else:
    print("Não temos o valor dessa fruta!")