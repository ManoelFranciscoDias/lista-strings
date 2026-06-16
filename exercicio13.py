#Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será
#mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma
#aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela,
#informando se o usuário ganhou ou perdeu o jogo.

import random
def carregar_palavras():
    with open("palavras.txt", "r") as arquivo:
        palavras = [linha.strip() for linha in arquivo]
    return palavras

def escolher_palavra(palavras):
    return random.choice(palavras)

def embaralhar_palavra(palavra):
    letras = list(palavra)
    random.shuffle(letras)
    return ''.join(letras)

def jogar_palavra_embaralhada():
    palavras = carregar_palavras()
    palavra_secreta = escolher_palavra(palavras)
    palavra_embaralhada = embaralhar_palavra(palavra_secreta)
    tentativas = 6

    print(f"Palavra embaralhada: {palavra_embaralhada}")

    while tentativas > 0:
        palpite = input("Digite seu palpite: ").lower()

        if palpite == palavra_secreta:
            print(f"Parabéns! Você adivinhou a palavra '{palavra_secreta}'!")
            break
        else:
            tentativas -= 1
            print(f"Palpite incorreto! Tentativas restantes: {tentativas}")

    if tentativas == 0:
        print(f"Game Over! A palavra era '{palavra_secreta}'.")

jogar_palavra_embaralhada()
