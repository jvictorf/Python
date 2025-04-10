# %%
# Faça um programa que conte quantas vezes a letra "A" aparece em uma palavra.

palavra = input("Digite uma palavra: ")

qtde = 0

for i in palavra:
    if i == "a":
        qtde += 1

print("A letra 'a' aparece", qtde, "vez(es) na palavra", palavra)