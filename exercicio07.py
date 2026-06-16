# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# a. quantos espaços em branco existem na frase.
# b. quantas vezes aparecem as vogais a, e, i, o, u.

frase = input("Digite uma frase: ")
espacos = frase.count(" ")
vogais = sum(frase.count(vogal) for vogal in "aeiouAEIOU")
print(f"A frase contém {espacos} espaços em branco.")
print(f"A frase contém {vogais} vogais.")