# Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela
# por extenso.

numero = int(input("Digite um número até 99: "))
if 0 <= numero <= 9:
    unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    print(unidades[numero])
elif 10 <= numero <= 19:
    especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    print(especiais[numero - 10])
elif 20 <= numero <= 99:
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezena = numero // 10
    unidade = numero % 10
    if unidade == 0:
        print(dezenas[dezena])
    else:
        print(f"{dezenas[dezena]} e {unidades[unidade]}")

