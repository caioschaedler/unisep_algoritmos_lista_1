###
# atividade 1
# Aluno: caio schaedler
# data 18/03/2024
###

valorcerca = float(input("digite o valor da cerca por metro:"))
largura = float(input("digite a largura do terreno (em metros): "))
comprimento = float(input("digite o comprimento do terreno (em metros): "))
totalterreno = (largura * 2) + (comprimento * 2)
total = totalterreno * valorcerca
print(f" o custo para cercar esse terreno eh: {total:.2f}")

