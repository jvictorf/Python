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

print(lista)
print(f"Maior número é: {maior_num} \n2Menor número é: {menor_num}")
print(f"Média dos números é: {media_num}")