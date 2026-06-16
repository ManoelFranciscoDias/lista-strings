# Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou
# vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são
# ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um
# programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.

frase = input("Digite uma frase: ")
frase_limpa = ''.join(frase.split()).lower()
if frase_limpa == frase_limpa[::-1]:
    print(f"A frase '{frase}' é um palíndromo.")

else:
    print(f"A frase '{frase}' não é um palíndromo.")

