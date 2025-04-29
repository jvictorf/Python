#%%
lista = []

while len(lista) < 10:
    numeros = input("Entre com 10 números: ")
    if numeros == "":
        print("Entrada vazia não é permitida. Por favor, insira um número.")
        continue
    try:
        lista.append(int(numeros))
    except ValueError:
        print("Por favor, digite um número válido.")

maior_num = max(lista)
menor_num = min(lista)
media_num = sum(lista) / len(numeros)
pares = [num for num in lista if num % 2 == 0]

print(lista)
print(f"Maior número é: {maior_num} \nMenor número é: {menor_num}")
print(f"Média dos números é: {media_num}")
print(f"Esse são os números pares: {pares}")