# 14. Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras,
# como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma
# subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e
# afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa
# que peça uma texto e transforme-o para a grafia leet speak.

def leet_speak(texto):
    leet_dict = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7'
    }
    texto_leet = ''.join(leet_dict.get(letra.lower(), letra) for letra in texto)
    return texto_leet

texto = input("Digite um texto para converter para leet speak: ")

texto_convertido = leet_speak(texto)
print(f"Texto em leet speak: {texto_convertido}")

