# %%

idade = int(input("Qual a sua idade? "))

if idade >= 70:
    print("Cuidado com a bebida!")
    print("Consulte o seu geriatra!")
elif idade >= 18:
    print("Você pode beber cerveja!")
    print("Beba com moderação")
elif idade == 17:
    print("Espere mais 1 ano!")
    print("Fique no refri!")
else:
    print("Você não pode beber!")
    print("Vá para casa beber leite!")