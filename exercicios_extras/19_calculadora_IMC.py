#%%
peso = float(input("Qual seu peso: "))
altura = float(input("Qual sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f} e você está abaixo do peso!")
elif imc < 24.9:
    print(f"Seu IMC é {imc:.2f} e você está com o peso normal!")
elif imc < 29.9:
    print(f"Seu IMC é {imc:.2f} e você está com sobrepeso!")
else:
    print(f"Seu IMC é {imc:.2f} e você está com obesidade!")
