# %%
# Faça um programa que conte quantas vogais tem em uma palavra.

palavra = input("Digite uma palavra: ")

qtde_vogais = 0

for i in palavra:
    if i in ["a", "e", "i", "o", "u",]:
        qtde_vogais += 1

print("As vogais 'a', 'e', 'i', 'o', 'u' aparece", qtde_vogais, "vezes na palavra", palavra)