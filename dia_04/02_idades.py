# %%

idades = []

while True:
    idade = input("Entre com a idade: ")
    if idade == "":
        break
    idades.append(int(idade))

print(idades)

media  = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print("Media:", media)
print("Minimo:", minimo)
print("Maximo:", maximo)
print("Qtde:", qtde)