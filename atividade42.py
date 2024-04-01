###
# atividade 1
# Aluno: caio schaedler
# data 18/03/2024

porcentagem_distribuidor = 0.12
porcentagem_impostos = 0.45

custo_fabrica = float(input("digite o custo de fabrica"))
custo_distribuidor = custo_fabrica * porcentagem_distribuidor
custo_impostos = custo_fabrica * porcentagem_impostos
custo_consumidor = custo_impostos + custo_distribuidor + custo_fabrica
print(f"o custo ao consumidor eh: {custo_consumidor:.2f}")