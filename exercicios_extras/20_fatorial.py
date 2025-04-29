#%%
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Informe o número desejado: "))

print(f"O fatorial de {numero} é {fatorial(numero)}")