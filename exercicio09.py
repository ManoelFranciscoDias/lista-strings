# Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
# e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

cpf = input("Digite um número de CPF no formato xxx.xxx.xxx-xx: ")
cpf_limpo = cpf.replace(".", "").replace("-", "")
if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
    print("CPF inválido.")
else:
    print("CPF válido.")

    