#Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
#Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

print(f"string 1: {string1} - comprimento: {len(string1)}")
print(f"string 2: {string2} - comprimento: {len(string2)}")

if len(string1) == len(string2):
    print("As strings possuem o mesmo comprimento.")
else:
    print("As strings não possuem o mesmo comprimento.")

if string1 == string2:
    print("As strings são iguais.")
else:
    print("As strings são diferentes.")