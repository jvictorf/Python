def soma(nota1:float, nota2:float, nota3:float)->float:
    return nota1 + nota2 + nota3

def media(nota1:float, nota2:float, nota3:float)->float:
    return soma(nota1, nota2, nota3) / 3

nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com o a segunda nota: "))
nota3 = float(input("Entre com o a terceira nota: "))

print(f"A média das notas é: {media(nota1, nota2, nota3)}")