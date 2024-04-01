###
# atividade 1
# Aluno: caio schaedler
# data 18/03/2024
###

nome_vendedor = input("informe o nome do vendedor: ")
numero_carros_vendidos = float(input("informe o numero de carros vendidos: "))
valor_total_vendas = float(input("informe o valor total das vendas: "))
salario = 500.0
comissao_carro = 50.0
comissao_venda = 0.05 * valor_total_vendas
salario_total = salario + (comissao_carro * numero_carros_vendidos) + comissao_venda
print (f"o salario do vender {nome_vendedor} eh: {salario_total:.2f}")
