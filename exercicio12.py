# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso
# deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço
# separador.

telefone = input("Digite um número de telefone: ")
telefone_limpo = telefone.replace("-", "")
if len(telefone_limpo) == 7 and telefone_limpo.isdigit():
    telefone_corrigido = "3" + telefone_limpo
    print(f"Número corrigido: {telefone_corrigido}")
else:
    print("Número de telefone inválido.")
