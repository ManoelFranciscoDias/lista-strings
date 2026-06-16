# 11. Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
# escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado. 

import random

def carregar_palavras():

    with open("palavras.txt", "r") as arquivo:
        palavras = [linha.strip() for linha in arquivo]
    return palavras

def escolher_palavra(palavras):
    return random.choice(palavras)

def jogar_forca():
    palavras = carregar_palavras()
    palavra_secreta = escolher_palavra(palavras)
    letras_adivinhadas = set()
    tentativas = 6

    while tentativas > 0:
        palavra_mostrada = ''.join(letra if letra in letras_adivinhadas else '_' for letra in palavra_secreta)
        print(f"Palavra: {palavra_mostrada}")
        print(f"Tentativas restantes: {tentativas}")

        letra = input("Digite uma letra: ").lower()

        if letra in palavra_secreta:
            letras_adivinhadas.add(letra)
            if all(letra in letras_adivinhadas for letra in palavra_secreta):
                print(f"Parabéns! Você adivinhou a palavra '{palavra_secreta}'!")
                break
        else:
            tentativas -= 1
            print("Letra incorreta!")

    if tentativas == 0:
        print(f"Game Over! A palavra era '{palavra_secreta}'.")

