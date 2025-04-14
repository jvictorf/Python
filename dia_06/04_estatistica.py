def soma(a:float, b:float, *args)->float:
    valores = [a, b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a, b, *args) / (len(args)+2)

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))
d = float(input("Entre com o valor de d: "))
e = float(input("Entre com o valor de e: "))

print(f"Média: {media(a, b, c, d, e)}")