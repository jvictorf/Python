# Faça um programa que receba 4 alturas usando um laço 
# de repetição e realize a soma dessas alturas.

# %%

soma = 0
qtde_entradas = 4

for i in range(qtde_entradas): #ou range(0, 4)
    altura = input("Entre com a altura: ")
    altura = float(altura)
    soma += altura

print("A soma das alturas é:", soma)