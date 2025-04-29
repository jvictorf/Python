#%%
def num_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numero = int(input("Entre com um número"))

if num_primo(numero):
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} não é primo")