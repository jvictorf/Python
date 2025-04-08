numero = int(input("Entre com um número inteiro para calcular a raiz quadrada: "))

raiz = numero ** 0.5 # ou numero ** (1/2)

raiz = round(raiz, 4)

print("Raiz quadrada de", numero, "é", raiz)