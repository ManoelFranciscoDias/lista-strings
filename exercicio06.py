#Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com
#o nome do mês por extenso.

data = input("Digite a data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = data.split("/")
meses = {
    "01": "Janeiro",
    "02": "Fevereiro",
    "03": "Março",
    "04": "Abril",
    "05": "Maio",
    "06": "Junho",
    "07": "Julho",
    "08": "Agosto",
    "09": "Setembro",
    "10": "Outubro",
    "11": "Novembro",
    "12": "Dezembro"
}
if mes in meses:
    print(f"{dia} de {meses[mes]} de {ano}")
else:
    print("Mês inválido.")
