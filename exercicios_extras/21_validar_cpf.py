#%%
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto1 = (soma1 * 10) % 11
    if resto1 == 10 or resto1 == 11:
        resto1 = 0
    if int(cpf[9]) != resto1:
        return False

    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto2 = (soma2 * 10) % 11
    if resto2 == 10 or resto2 == 11:
        resto2 = 0
    if int(cpf[10]) != resto2:
        return False

    return True

cpf = input("Informe seu cpf: ")

if validar_cpf(cpf):
    print(f"O CPF {cpf} é válido!")
else:
    print(f"O CPF {cpf} é inválido!")